

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

# for i in df_.columns:
#     print(i, df_.columns.to_list().index(i))

# CREATING THE PAIRS TO BE ANALYSED
hold_combo = []

for i in df_.columns[2:]:
    for ii in df_.columns[2:]:
        if i != ii:
            hold_combo.append((i, ii))

hold_combo_len = len(hold_combo)

# print(hold_combo)

df_.replace(np.nan, 0, inplace=True)

for i in df_.columns:
    if df_[i].dtype != 'object' and i != 'COMMUNITY_AREA_NUMBER':
        df_[i].replace(0, df_[i].mean(), inplace=True)

df_.iloc[77, 0]  = 78

axes = []
axes_tup = []

for i in range(hold_combo_len):
    axes.append('ax' + str(i + 1))

for i in range(len(axes)):
    if i == 0 or i % 4 == 0 and i != 40:
        axes_tup.append("(" + axes[i] + ", " + axes[i+1] + ", " + axes[i+2] + ", " + axes[i+3] + ")")

# print(", ".join(i for i in axes_tup))


# FINDING HIGHLY CORRELATED PAIRS
axes_with_high_corr = [] # index of pairs that have high correlation

for num, (i, ii) in enumerate(hold_combo, start=1):

    corr, p_val = stats.pearsonr(df_[i], df_[ii])
    mean_i = df_[i].mean()
    mean_ii = df_[ii].mean()

    cov_xy = sum((df_[i] - mean_i) * (df_[ii] - mean_ii)) / df_[i].count()

    if corr > 0.8 or corr < -0.8 and num < 41:
        axes_with_high_corr.append('ax'+ str(num))
        axes_with_high_corr.append('ax' + str(num*2))
        print(f'{num}. Correlation: {corr}, P_val: {p_val}')
        # print(f'cov_xy: {cov_xy}')

# print(", ".join(axes_with_high_corr))


# GRAPHING THE REGRESSION LINE AND RESIDUAL PLOT OF HIGHLY CORRELATED PAIRS
# figure, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16)
#          , (ax17, ax18, ax19, ax20), (ax21, ax22, ax23, ax24), (ax25, ax26, ax27, ax28), (ax29, ax30, ax31, ax32)
#          , (ax33, ax34, ax35, ax36), (ax37, ax38, ax39, ax40)) = plt.subplots(10, 4)


# hold_axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13, ax14, ax15, ax16, ax17, ax18, ax19,
#          ax20, ax21, ax22, ax23, ax24, ax25, ax26, ax27, ax28, ax29, ax30, ax31, ax32, ax33, ax34, ax35, ax36, ax37,
#          ax38, ax39, ax40]

figure, ((ax3, ax8, ax12), (ax14, ax19, ax24), (ax36, ax38, ax40)) = plt.subplots(3, 3)
hold_axes = [ax3, ax8, ax12, ax14, ax19, ax24, ax36, ax38, ax40] # high corr ±0.8

for i in range(len(hold_axes)):
    sns.regplot(df_[hold_combo[i][0]], df_[hold_combo[i][1]], ax=hold_axes[i])

# --
figure2, ((ax6, ax16, ax24), (ax28, ax38, ax48), (ax64, ax76, ax80)) = plt.subplots(3, 3)
hold_axes2 = [ax6, ax16, ax24, ax28, ax38, ax48, ax64, ax76, ax80]

for i in range(len(hold_axes)):
    sns.residplot(df_[hold_combo[i][0]], df_[hold_combo[i][1]], ax=hold_axes2[i])


plt.show()