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