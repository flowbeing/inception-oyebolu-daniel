# The aim of this is to help me understand how probability plays out over large amount of trials or phenomenon
import pandas as pd
from random import randint
from matplotlib import pyplot as plt
import seaborn as sns
from math import sqrt
import numpy as np
from scipy import stats

outcome = []

trial_num = 1000000

while len(outcome) < trial_num:
    outcome.append(randint(0, 36))

prob_each = 1 / 37

print(f"Probability of choosing each number i.e Probability of winning: {prob_each}")
print(f"Probability of losing: {1 - prob_each}")

table = {
    'num': [],
    'Occurences': []
}


for i in set(outcome):
    table['num'].append(i)
    table['Occurences'].append(outcome.count(i))

df = pd.DataFrame(table)

mean_occur = df.Occurences.mean()
df['dev from mean'] = df['Occurences'] - mean_occur
df['dev squared'] = df['dev from mean'] ** 2
var = df['dev squared'].sum() / df['num'].count()

df.sort_values(by=['Occurences'], inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head(50))
print(f"Min Occur: {df.Occurences.min()}")
print(f"Max Occur: {df.Occurences.max()}")
print(f"Mean Occur: {mean_occur}")
# print(f"Variance: {var}")
print(f"Standard dev: {sqrt(var)}")
print(f"Mean absolute deviation: {abs(df['dev from mean']).sum() / df['dev from mean'].count()}")

print()
print("LESSONS")
print('Increasing your number of trials does not increase your probability of winning\n'
      'It only exponents your winnings | losses with your probability of winning or losing')

print()
print('OBSERVING THE GROUPBY() METHOD')
group_by = [i for i in df.columns if df[i].dtype == 'int64' or df[i].dtype == 'object']
print(group_by)

df.groupby(group_by, as_index=False).mean()
mean_occur = df.Occurences.mean()
df['dev from mean'] = df['Occurences'] - mean_occur
df['dev squared'] = df['dev from mean'] ** 2
var = df['dev squared'].sum() / df['num'].count()


print(df.head(50))
print(f"Min Occur: {df.Occurences.min()}")
print(f"Max Occur: {df.Occurences.max()}")
print(f"Mean Occur: {mean_occur}")
# print(f"Variance: {var}")
print(f"Standard dev: {sqrt(var)}")

print()
print("Correlation")
print(f"{df[['Occurences', 'dev from mean']].corr()}")

print()
occurences = df.Occurences.to_frame()
occurences.columns = ['Column Names']
occurences.reset_index(drop=True, inplace=True)

occurences.sort_values(by=['Column Names'], ascending=False, inplace=True)

print(occurences.head(50))

df_ = df[['num', 'Occurences', 'dev from mean']]

print()
p_table = df_.pivot(index='num', columns='Occurences')
p_table.fillna(0, inplace=True)

# print(df.columns)
# print(p_table.columns)

print(p_table)

# print()
# print(df.index)
# print(p_table.index)



fig, ax = plt.subplots()
ax.pcolor(p_table, cmap='RdBu')

#label names
col_labels = p_table.columns.levels[1]
row_labels = p_table.index

#move ticks and labels to the center
ax.set_xticks(np.arange(p_table.shape[1]) + 1, minor=False)
ax.set_yticks(np.arange(p_table.shape[0]) + 1, minor=False)

#insert labels
ax.set_xticklabels(col_labels, minor=False)
ax.set_yticklabels(row_labels, minor=False)

#rotate label if too long
# plt.xticks(rotation=90)

fig.colorbar(ax.pcolor(p_table, cmap='RdBu'))
plt.show()

print(np.arange(p_table.shape[1]) + 0.5)

corr_ = stats.pearsonr(df['num'], df['Occurences'])
print(corr_)