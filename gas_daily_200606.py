import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# open csv file as pd
df = pd.read_csv('GW_pricip/gas_concent_daily_2006.csv', encoding='cp949', index_col=0)

# Convert the index to a datetime object
df.index = pd.to_datetime(df.index)

# calculate total mean of column SO2(ppb), NOx(ppb)
gas_mean = df.mean()

fig, ax1 = plt.subplots()
fig.set_figheight(5)
fig.set_figwidth(12)

ax2 = ax1.twinx()

# draw line graph of daily nc_data from June of SO2(ppb) & NOx(ppb)
line_1 = ax1.plot(df.index.strftime('%d'), df['SO2(ppb)'], label='SO2', color='blue')
line_2 = ax2.plot(df.index.strftime('%d'), df['NOx(ppb)'], label='NOx', color='red')
lines = line_2 + line_1

# draw average line of SO2(ppb), NOx(ppb)
ax1.axhline(gas_mean['SO2(ppb)'], linestyle='--', color='blue', linewidth=0.5)
ax2.axhline(gas_mean['NOx(ppb)'], linestyle='--', color='red', linewidth=0.5)

ax1.set_ylabel('SO2 (ppb)')
ax2.set_ylabel('NOx (ppb)')

plt.xticks(np.arange(0, 31, 5))

plt.title('Daily Concentration of gas (2006-06)')

labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

# plt.show()
plt.savefig('gas_daily_200606.png')
