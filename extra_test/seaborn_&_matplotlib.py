import pandas as pd
import numpy as np
import seaborn
from matplotlib import pyplot as plt
import sqlalchemy

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns',10)

data_frame = pd.read_csv('/Users/G/OneDrive/DS/Data/DS/Companies.csv')

des = data_frame.describe()

print(des)

print()
print(data_frame)

# print(data_frame)
fig, ax = plt.subplots()
plot_one = data_frame.plot('Name', 'Employee | friend recommendation', ax=ax)
plot_two = data_frame.plot('Name', 'Employee CEO approval rate', ax=ax)

# plot.set_xlim([0, 70])
plt.show()

sqlalchemy.