import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn

df = pd.read_csv('/Users/G/OneDrive/DS/Data/countries_stat.csv')

#  print(df[['Country', 'Population', 'GDP ($ per capita)']])
#  seaborn.swarmplot('GDP ($ per capita)', 'Population', data=df)

#  plt.show()

# print(df['GDP ($ per capita)'].describe(include='all'))

# print(df.head(20))

new_df = df.head(10)

# print(new_df.dropna(axis=0))

extra_df = df[['Country', 'Population', 'Area (sq. mi.)']]
# print(extra_df.head(50))

# idxmax_population = extra_df['Population'].idxmax()
# print(idxmax_population)

# print(extra_df.at[42:43, 'Population'])
# print(extra_df.nan)

# print(df['Population']/5)
# print(5/df['Population'])

# df['Service'] = df['Service'].astype('int', copy=True)



# print(df.dtypes)



#print(new_df.dropna(subset=['Service']))

bins = np.linspace(df['Population'].min(), df['Population'].max(), 4, retstep=False)
labels = ['low', 'average', 'high']
df['label'] = pd.cut(df['Population'], bins, labels=labels, include_lowest=False)


# print(df['Population'].to_list())
df.rename(columns={'label' : 'P_label'}, inplace=True)
# df['Service'].replace(',', '.', inplace=True)
# print(df.dtypes)
# df['Service'].astype('float')

# df.replace(np.nan, df['Service'].mean(axis=0), inplace=True)

# df.dropna(subset=['Service'], axis=0, inplace=True)
print(df['Service'].head(40))

print(df['Service'].value_counts().idxmax())
# print(df['Population'].idxmax())

print(type(df.dropna(subset=['Service'], axis=0, inplace=True)))
df.reset_index(drop=False, inplace=True)
print(df[['Country', 'Population', 'Service']].head(50))

# plt.hist(df['Service'])
# plt.show()
print(np.linspace(1, 5, 5, retstep=True, endpoint=False))
# print(df.columns.value_counts())
df.drop('P_label', axis=1, inplace=True)

# print(pd.get_dummies(df['Country']))
df[['Service']].astype('int')
# print(df.head())


# print(df.describe(include='all'))
# df['label'] = None
# print(df.to_csv('/Users/G/Desktop/xtraction.csv'))

summarised = df[['Country', 'Population', 'Service']]

grouped_summary = summarised.groupby(['Country', 'Population'], as_index=True)

print(df.Service.value_counts())

print(grouped_summary)

seaborn.regplot('Population', 'Service', data=summarised)
plt.show()
# print(df['Population'].min(), df['Population'].max())