import numpy as np
import pandas as pd
import matplotlib.pyplot as plt, matplotlib.dates as dates

# read ion_concent_daily_2006.csv as pd
df = pd.read_csv('GW_pricip\ion_concent_daily_2006.csv', encoding='cp949', index_col= 0)

# Convert the index to a datetime object
df.index = pd.to_datetime(df.index)

# calculate total mean of column of NO3-, SO42-, NH4+
ion_mean = df.mean()

plt.figure(figsize=(10, 5))
df = df.loc['2006-03-16':'2006-06-25']

# draw line graph of daily data from 2006-04-19 to 2006-06-25 of NO3-
plt.plot(df.index.strftime('%m-%d'), df['NO3-'], label='NO3-', color = 'red')
# draw line graph of daily data from 2006-04-19 to 2006-06-25 of SO42-
plt.plot(df.index.strftime('%m-%d'), df['SO4-'], label='SO42-', color = 'blue')
# draw line graph of daily data from 2006-04-19 to 2006-06-25 of NH4+
plt.plot(df.index.strftime('%m-%d'), df['NH4+'], label='NH4+', color = 'green')


plt.axhline(ion_mean['NO3-'], linestyle=':', color = 'red', linewidth=0.5)
plt.axhline(ion_mean['SO4-'], linestyle='--', color = 'blue', linewidth=0.5)
plt.axhline(ion_mean['NH4+'], linestyle='--', color = 'green', linewidth=0.5)

plt.xlabel('Date')

plt.xlabel('Date')
plt.ylabel('Ion Concentration (μeq/L)')
plt.title('Daily Concentration of ions (2006)')

plt.legend()

plt.tight_layout()

# plt.show()
plt.savefig('daily_concent_ion_2006.png')