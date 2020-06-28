import pandas as pd

data = {
    'table one': [2,3,7,2,6],
    't1_DFM': ['-', '-', '-', '-', '-'],
    'table two': [10,8,7,5,10],
    't2_DFM': ['-', '-', '-', '-', '-'],
    'table three': [10, 13, 14, 13, 15],
    't3_DFM': ['-', '-', '-', '-', '-']
}

df = pd.DataFrame(data)
df.columns.name = 'No'

print()
print('FIRST TABLE')
print(df.head())

m_t1 = int(df['table one'].mean())
m_t2 = int(df['table two'].mean())
m_t3 = int(df['table three'].mean())

print()
print(f"Mean 1: {m_t1}\n"
      f"Mean 2: {m_t2}\n"
      f"Mean 3: {m_t3}")

df['t1_DFM'] = df['table one'] - m_t1
df['t2_DFM'] = df['table two'] - m_t2
df['t3_DFM'] = df['table three'] - m_t3

# df.columns = ['table one', 't1_DFM', 'table two', 't2_DFM', 'table three', 't3_DFM']

print()
print('SUM OF SQUARES WITHIN GROUPS')
print(df.head())

ss_t1 = sum(df['t1_DFM']**2)
ss_t2 = sum(df['t2_DFM']**2)
ss_t3 = sum(df['t3_DFM']**2)

print()
print(f"Sum of Squares t1: {ss_t1}\n"
      f"Sum of Squares t2: {ss_t2}\n"
      f"Sum of Squares t3: {ss_t3}\n"
      f"\n"
      f"Sum of Squares Within Groups i.e sum of Sum of Squares: {ss_t1 + ss_t2 + ss_t3}")

list_all_data = df['table one'].to_list() + df['table two'].to_list() + df['table three'].to_list()

all_data = pd.DataFrame({'All data': list_all_data})
all_datamean = all_data['All data'].mean()
all_data['DFM'] = all_data['All data'] - all_datamean
all_data['DFM sqrd'] = all_data['DFM'] ** 2

ss_alldata = all_data.sum()

print('ALL DATA')
print(all_data)

print()
print(f"          Mean (All data) : {all_datamean}")
print(f"Sum of Squares (All data) : {all_data['DFM sqrd'].sum()}")