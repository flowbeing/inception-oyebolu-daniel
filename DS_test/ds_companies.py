import pandas as pd
import numpy as np
import seaborn
from matplotlib import pyplot as plt

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns',10)

data_frame = pd.read_csv('/Users/G/OneDrive/DS/Data/DS/Companies.csv')


print(data_frame)
plot = seaborn.barplot('Name', 'Employee CEO approval rate', data=data_frame)
plot.set_xlim([0, 70])
plt.show()