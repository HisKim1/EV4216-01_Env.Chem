import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
from netCDF4 import Dataset
from pathlib import Path
from numpy import datetime64
import utils
import os
import PIL.Image



# open GW_pricip\interim_daily_200606.nc using netCDF4
nc_data = Dataset(r'GW_pricip/interim_daily_200606.nc')

# open GW_pricip\interim_daily_200606.nc using xarray
clim_data = xr.open_dataset(r'GW_pricip/interim_daily_200606.nc')
clim_data = clim_data.sortby('time')
clim_data = clim_data.resample(time='D').mean()

ion_con = pd.read_csv(r'GW_pricip/ion_concent_daily_2006.csv', encoding='cp949', index_col= 0)
ion_con.sort_index(inplace=True)


# gas_con = xr.open_dataset(r'GW_pricip/gas_con2.nc')
# gas_con['time'] = gas_con['time'].astype('datetime64[ns]')
# gas_con = gas_con.to_netcdf(r'GW_pricip/gas_con.nc')

gas_con = pd.read_csv(r'GW_pricip/gas_concent_daily_2006.csv', encoding='cp949', index_col=0)


# ******************************************************
# begin: plot daily temperature on June 2006 using xarray
# ******************************************************
# dt_t2m = clim_data['t2m'] - 273.15
# dt_lat = dt_t2m.latitude
# dt_lon = dt_t2m.longitude
# dt_time = pd.date_range('2006-06-01', '2006-06-30', freq='D').day

# ******************************************************
# setup the plot using cartopy
# ******************************************************
# val_min = np.min(dt_t2m[100:140, 20:50])
# val_max = np.max(dt_t2m[100:140, 20:50])
#
# for day in dt_time:
#     utils.xr_plot_climatology(dt_t2m[day - 1, :, :],
#                               'xr_t2m' + str(day),
#                               'xr_t2m' + str(day) + '.png',
#                               val_min, val_max,
#                               100, 25,
#                               40, 25
#                               )
#
#     new_frame = PIL.Image.open(r'xr_t2m' + str(day) + '.png')
#     image_frames.append(new_frame)
#
# utils.save_gif(image_frames, r'xr_t2m.gif', 200)

# ******************************************************
# end
# ******************************************************

# cut clim_data in range of latitude 25~50, longitude 100~140
clim_data = clim_data.sel(latitude=slice(51, 24), longitude=slice(99, 141))
#

daily_mean_t2m = clim_data['t2m'] - 273.15
daily_mean_t2m.attrs['units'] = 'Degree Celsius'

# pnt_t2m = daily_mean_t2m.stack(point=('latitude', 'longitude')).to_numpy().squeeze().T
# SO2_con = np.repeat(gas_con['SO2(ppb)'].to_numpy()[:, np.newaxis], 2109, axis=1).reshape(30, 2109).T
# corr_t2m = utils.pearsonr_corr(pnt_t2m, SO2_con)


pnt_t2m = daily_mean_t2m
SO2_con = gas_con['SO2(ppb)']
corr_t2m = utils.cor3(pnt_t2m, SO2_con)

utils.xr_plot_climatology(corr_t2m,
                          't2m',
                          't2m_corr.png',
                          -1,
                          1,
                          100,25,
                          40,25)

# plt.plot(result['sp'])

for var in clim_data.var():
    print(f'start {var}')
    tmp_var = clim_data[var]
    utils.xr_plot_climatology(utils.cor3(tmp_var, SO2_con),
                              f'{clim_data[var].long_name}',
                              f'corr_{var}.png',
                              -1,
                              1,
                              100, 25,
                              40, 25)