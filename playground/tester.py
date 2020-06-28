import pandas as pd
import numpy as np
from math import sqrt
from scipy import stats
from random import randint
import time
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

file = 'http://data.cityofchicago.org/resource/jcxq-k9xf.csv'

df_ = pd.read_csv(file)

for i in df_.columns:
    print(i, df_.columns.to_list().index(i))

hold_combo = []

for i in df_.columns:
    for ii in df_.columns:
        if i != ii:
            hold_combo.append((i, ii))

df_.replace(np.nan, 0, inplace=True)

for i in df_.columns:
    if df_[i].dtype != 'object' and i != 'COMMUNITY_AREA_NUMBER':
        df_[i].replace(0, df_[i].mean(), inplace=True)

df_.iloc[77, 0]  = 78


print(df_.tail(20))
print()

# randint(1, 50) for i in range(5000)
data = {
    'x': df_['per_capita_income_'].to_list(), # 'x': [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
    'y': df_[df_.columns[6]].to_list(), # 'y': [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]
    'x sqrd': ['-' for i in range(df_['per_capita_income_'].count())],
    'y sqrd': ['-' for i in range(df_['per_capita_income_'].count())],
    'dev from mean (x)': ['-' for i in range(df_['per_capita_income_'].count())],

    # ".|": [".|" for i in range(10)],
    'dev from mean (y)': ['-' for i in range(df_['per_capita_income_'].count())],
    'dev_x̄ * dev_ȳ': ['-' for i in range(df_['per_capita_income_'].count())],
    'dev from mean (x) sqrd': ['-' for i in range(df_['per_capita_income_'].count())],
    'dev from mean (y) sqrd': ['-' for i in range(df_['per_capita_income_'].count())],

    # "|.": ["|." for i in range(10)]
}

df = pd.DataFrame(data)
df.sort_values(by=['x'], ascending=True, inplace=True)

# print(df.head(20))

mean_x = df['x'].mean()
mean_y = df['y'].mean()


df['x sqrd'] = df['x'] ** 2
df['y sqrd'] = df['y'] ** 2

df['dev from mean (x)'] = df['x'] - mean_x
df['dev from mean (y)'] = df['y'] - mean_y


df['dev_x̄ * dev_ȳ'] = df['dev from mean (x)'] * df['dev from mean (y)']

df['dev from mean (x) sqrd'] = df['dev from mean (x)'] ** 2
df['dev from mean (y) sqrd'] = df['dev from mean (y)'] ** 2

variance_x =  sum(df['dev from mean (x) sqrd']) / df['dev from mean (x)'].count() # Population variance
variance_y =  sum(df['dev from mean (y) sqrd']) / df['dev from mean (y)'].count() # Population variance

codev_xy = sum(df['dev from mean (x)'] * df['dev from mean (y)'])
cov_xy = sum(df['dev from mean (x)'] * df['dev from mean (y)']) / df['dev from mean (x)'].count() # Population covariance

std_x = sqrt(variance_x)
std_y = sqrt(variance_y)

df['dev_x̄ sqrd * dev_ȳ sqrd'] = df['dev from mean (x) sqrd'] * df['dev from mean (y) sqrd'] ###
df['sqrt(dev_x̄ sqrd * dev_ȳ sqrd)'] = [sqrt(i) for i in df['dev_x̄ sqrd * dev_ȳ sqrd']] ###


print(df.head(20))

print()
print(f"mean_x: {mean_x}")
print(f"mean_y: {mean_y}")

print()
print(f"Population variance_x  : {variance_x}")
print(f"Population variance_y  : {variance_y}")

print()
print(f"Population codeviation    : {codev_xy}")
print(f"Population covariance (/n): {cov_xy}")

print()
# print(f"Sqrt(cov(x,y)): {sqrt(cov_xy)}")

print()
numerator = sum(df['dev_x̄ * dev_ȳ'])
denominator = sqrt(sum(df['dev from mean (x) sqrd']) * sum(df['dev from mean (y) sqrd']))

print(f"Numerator   i.e sum(dev_x̄ * dev_ȳ)                         : {numerator}")
print(f"Denominator i.e sqrt(∑( (dev_x̄)**2 ) x ∑( (dev_ȳ)**2) ) )  : {denominator}")

print()
c_coef, p_val = stats.pearsonr(df['x'], df['y'])
print(f"Correlation_manual  : {numerator / denominator}")
print(f"Coreelation_manual_2: {cov_xy / (std_x * std_y)}")
print(f"Correlation_pandas  : {df[['x', 'y']].corr(method='pearson').iloc[0,1]}")
print(f"Correlation_scipy   : {c_coef}, {p_val}")

# print(f"Correlation: {sum(df.x * df.y) / sqrt(sum(df['x sqrd']) * sum(df['y sqrd']) )}")


print()
print("SUMMATION")
print()
print(f"∑(x) + ∑(y) = ∑(x+y): {df.x.sum() + df.y.sum()} = {sum(df.x + df.y)}")
print()
print("MULTIPLICATION")
print()
print(f"∑(x) * ∑(y) ≠ ∑(x*y)                      : {df.x.sum() * df.y.sum()} ≠ {sum(df.x * df.y)}")
print(f"∑(x) * ∑(y) ≠ sqrt(∑(x sqrd) * ∑(y sqrd)) : "
      f"{sum(df.x) * sum(df.y)} ≠ {sqrt(sum(df['x sqrd']) * sum(df['y sqrd']) )}")
print()
print('    deviation values')
print("    ----------------")
print(f"    (∑(dev_x̄ * dev_ȳ))**2 ≠ ∑(dev_x̄ sqrd * dev_ȳ sqrd)  : "
      f"i.e {(sum(df['dev from mean (x)'] * df['dev from mean (y)']))**2} ≠ "
      f"{(df['dev_x̄ sqrd * dev_ȳ sqrd'].sum())} \n"
      f"    i.e \n"
      f"    ∑(dev_x̄ * dev_ȳ)) ≠ sqrt(∑(dev_x̄ sqrd * dev_ȳ sqrd)): i.e {(sum(df['dev from mean (x)'] * df['dev from mean (y)']))} ≠ {(df['dev_x̄ sqrd * dev_ȳ sqrd'].sum())**(1/2)}") ###


fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

# sns.regplot(df['x'], df['y'], ax=ax1)
# sns.residplot(df['x'], df['y'], ax=ax1)
# sns.distplot(df['dev from mean (x)'], kde=False, ax=ax1)
# sns.distplot(df['dev from mean (x)'], ax=ax2)
# sns.distplot(df['x'], ax=ax3)
#sns.distplot(df['x'], ax=ax3)
# plt.show()


sns.regplot('x', 'y', data=df, ax=ax1)
sns.residplot('dev from mean (x)', 'dev from mean (y)', data=df, ax=ax2)
sns.distplot(df['dev from mean (x)'], ax=ax3)
sns.distplot(df['dev from mean (y)'], ax=ax4)
plt.show()