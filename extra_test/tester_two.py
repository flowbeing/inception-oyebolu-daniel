import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from random import randint

hold_it = sorted(randint(1, 1000) for r in range(100))

dataframe = {
    'Values' : hold_it
}

df = pd.DataFrame(dataframe)

mean = df['Values'].mean()
print(mean)

print()
df['dist from mean'] = df['Values'] - mean

df['dist from mean (abs)'] = abs(df['Values'] - mean)

print(df.head(50))
print(df.tail(50))
# print(df.head(50))
# print(df.tail(50))

print()

print(f"real mean : {df['Values'].mean()}")

print(df['dist from mean'].iloc[0:50].mean())

print(df['dist from mean'].iloc[50:100].mean())

print(df['dist from mean'].sum())

dataframe_two = {
    'dist from mean_one' : df['dist from mean'].iloc[0:50].to_list(),
    'dist from mean_two' : df['dist from mean'].iloc[50:100].to_list()[::-1]
}

new_df = pd.DataFrame(dataframe_two)

see = (ii - i for i, ii in zip(dataframe_two['dist from mean_one'], dataframe_two['dist from mean_two']))

print(dataframe_two['dist from mean_one'])
print(dataframe_two['dist from mean_two'])

print(dataframe_two['dist from mean_two'][0] - dataframe_two['dist from mean_one'][0])

new_df['difference'] = new_df['dist from mean_one'] + new_df['dist from mean_two']
print(new_df)

print(f'Deficit = {new_df["dist from mean_one"].sum()}')
print(f'Surplus = {new_df["dist from mean_two"].sum()}')
print(f'sum difference = {new_df["difference"].sum()}')

print()
print('VALUE COUNT')
upto_100 = df[['Values']][df['Values'] < 101]['Values'].count()
upto_200 = df[['Values']][df['Values'] < 201]['Values'].count() - upto_100
upto_300 = df[['Values']][df['Values'] < 301]['Values'].count() - upto_200 - upto_100
upto_400 = df[['Values']][df['Values'] < 401]['Values'].count() - upto_300 - upto_200 - upto_100
upto_500 = df[['Values']][df['Values'] < 501]['Values'].count() - upto_400 - upto_300 - upto_200 - upto_100
upto_600 = df[['Values']][df['Values'] < 601]['Values'].count() - upto_500 - upto_400 - upto_300 - upto_200 - upto_100
upto_700 = df[['Values']][df['Values'] < 701]['Values'].count() - upto_600 - upto_500 - upto_400 - upto_300 - upto_200 \
           - upto_100
upto_800 = df[['Values']][df['Values'] < 801]['Values'].count() - upto_700 - upto_600 - upto_500 - upto_400 - upto_300 \
           - upto_200 - upto_100
upto_900 = df[['Values']][df['Values'] < 901]['Values'].count() - upto_800 - upto_700 - upto_600 - upto_500 - upto_400 \
           - upto_300 - upto_200 - upto_100
upto_1000 = df[['Values']][df['Values'] < 1001]['Values'].count() - upto_900 - upto_800 - upto_700 - upto_600 \
            - upto_500 - upto_400 - upto_300 - upto_200 - upto_100

dataframe_three = {
    'income' : np.linspace(100, 1000, 10),
    'Num of people earning this'  :   [upto_100, upto_200, upto_300, upto_400, upto_500, upto_600, upto_700,
                                                 upto_800, upto_900, upto_1000]
}

df_three = pd.DataFrame(dataframe_three)

df_three['Total earnings'] = df_three['income'] * df_three['Num of people earning this']
print(df_three)

print('SEGMENT CONTROL')

def seg_power(income): # How much power does a income class have over others in terms of how many people it can acquire.
    income_index = df_three['income'].to_list().index(income)
    df_three['seg_power'] = df_three.iloc[income_index, 2]  / df_three['income']
    print(df_three)

seg_power(500)

sns.barplot()
plt.show()

plt.boxplot(df['Values'])
plt.show()