import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import xarray as xr
from netCDF4 import Dataset
from pathlib import Path
import utils
import os
import PIL.Image

# open GW_pricip\interim_daily_200606.nc using netCDF4
nc_data = Dataset(r'GW_pricip/interim_daily_200606.nc')

# open GW_pricip\interim_daily_200606.nc using xarray
xr_data = xr.open_dataset(r'GW_pricip/interim_daily_200606.nc')
xr_data = xr_data.sortby('time')

ion_con = pd.read_csv(r'GW_pricip/ion_concent_daily_2006.csv', encoding='cp949', index_col= 0)
ion_con.sort_index(inplace=True)

os.chdir(r'result')

# ******************************************************
# netCDF4 : declare the variables in the dataset
# ******************************************************
# nc_lat = nc_data.variables['latitude'][:]
# nc_lon = nc_data.variables['longitude'][:]
# nc_time = nc_data.variables['time'][:]
# nc_t2m = nc_data.variables['t2m'][:]
# nc_msl = nc_data.variables['msl'][:]
# nc_u10 = nc_data.variables['u10'][:]
# nc_v10 = nc_data.variables['v10'][:]

# convert temperature unit from Kelvin to Celsius
# nc_t2m = nc_t2m - 273.15

# convert sea level pressure unit from Pa to hPa
# nc_msl = nc_msl / 100
#
# t2m_min = np.min(nc_t2m)
# t2m_max = np.max(nc_t2m)
# image_frames = []

# for day in range(0, 30):
#     day += 1
#     title = 't2m' + str(day)
#     # set variables to plot
#     utils.nc_plot_climatology(nc_t2m[day-1], title, title + '.png', t2m_min, t2m_max, nc_lon, nc_lat)
#
#     # append result and make gif
#     new_frame = PIL.Image.open(r't2m' + str(day) + '.png')
#     image_frames.append(new_frame)
#
# # combine images to gif
# utils.save_gif(image_frames, r't2m.gif', 150)
# image_frames.clear()


# ******************************************************
# xarray: declare the variables in the dataset
# ******************************************************
# dt_t2m = xr_data['t2m'] - 273.15
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

result = utils.calculate_lead_lag_correlation(ion_con.loc['2006-06-20'], xr_data, 'NO3-')

plt.plot(result['sp'])

