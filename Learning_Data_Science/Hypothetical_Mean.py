import pandas as pd

# Meant to calculate the mean assuming the values of Income pan out equally in
# 'Population_Mean_using_Hypothetical_income.py

listing  = []

for i in range(100):
    for ii in range(10):
        listing.append(i)

dicting = {
    'values': listing
}

df = pd.DataFrame(dicting)
mean = df['values'].mean()