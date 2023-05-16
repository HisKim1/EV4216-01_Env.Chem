import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read ion_concent_1997-2021.csv as pd
# 3 : NO3-, 4 : SO42-, 5 : NH4+
df = pd.read_csv('GW_pricip\ion_concent_1997-2021.csv', encoding='cp949', index_col= 0)

# calculate total mean of column of NO3-, SO42-, NH4+
ion_mean = df.mean()

# plot annual nc_data of column of NO3-, SO42-, NH4+
plt.figure(figsize=(8, 5))
plt.plot(df['3'], label='NO3-', color = 'red')
plt.plot(df['4'], label='SO42-', color = 'blue')
plt.plot(df['5'], label='NH4+', color = 'green')
plt.axhline(ion_mean['3'], linestyle='--', color = 'red', linewidth=0.5)
plt.axhline(ion_mean['4'], linestyle='--', color = 'blue', linewidth=0.5)
plt.axhline(ion_mean['5'], linestyle='--', color = 'green', linewidth=0.5)
plt.vlines(2006, 15, 100, linestyle='--', color = 'black', linewidth=2)

plt.xlabel('Year')
plt.xlim(1996, 2022)
plt.xticks(np.arange(1997, 2022, 2))


plt.ylabel('Concentration (μeq/L)')

plt.title('Annual Concentration of ions (1997-2021)')

plt.legend()
plt.savefig('ann_concent_ion.png')

print(df.loc[2006, ['3', '4', '5']])
print(ion_mean[['3', '4', '5']])
