import pandas as pd
import xarray as xr
from netCDF4 import Dataset
import utils
import PIL.Image

# open GW_pricip\interim_daily_200606.nc using netCDF4
nc_data = Dataset(r'GW_pricip/interim_daily_200606.nc')

# open GW_pricip\interim_daily_200606.nc using xarray
clim_data = xr.open_dataset(r'GW_pricip/interim_daily_200606.nc')
clim_data = clim_data.sortby('time')
clim_data = clim_data.resample(time='D').mean()

ion_con = pd.read_csv(r'GW_pricip/ion_concent_daily_2006.csv', encoding='cp949', index_col= 0)
ion_con.sort_index(inplace=True)

gas_con = pd.read_csv(r'GW_pricip/gas_concent_daily_2006.csv', encoding='cp949', index_col=0)

# ******************************************************
# begin: plot daily temperature on June 2006 using xarray
# ******************************************************

# setup the plot using cartopy
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

for var in clim_data.var():
    print(f'start {var}')
    tmp_var = clim_data[var]
    utils.xr_plot_climatology(utils.cor3(tmp_var, gas_con['SO2(ppb)']),
                              f'corr_{clim_data[var].long_name}&SO2',
                              f'corr_{var}&SO2.png',
                              -1,
                              1,
                              100, 25,
                              40, 25)

for var in clim_data.var():
    print(f'start {var}')
    tmp_var = clim_data[var]
    utils.xr_plot_climatology(utils.cor3(tmp_var, gas_con['NOx(ppb)']),
                              f'corr_{clim_data[var].long_name}&NOx',
                              f'corr_{var}&NOx.png',
                              -1,
                              1,
                              100, 25,
                              40, 25)