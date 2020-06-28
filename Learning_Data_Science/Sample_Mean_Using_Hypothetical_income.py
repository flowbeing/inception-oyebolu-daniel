from Learning_Data_Science import Hypothetical_Mean
from Learning_Data_Science.Population_Mean_using_Hypothetical_income import df, n, var
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
from math import sqrt

vals = list(set(df.Income.to_list()))

# if n < 1001:
#     occur = (df.Income.value_counts() / n) * (n/10)
# elif n > 1000:
#     occur = (df.Income.value_counts() / n) * (100)

occur = (df.Income.value_counts() / n) * (1000)

dictionary = {
    'Income': [],
    'Occur': []
}

for i, ii in zip(vals, occur):
    dictionary['Income'].append(i)
    dictionary['Occur'].append(ii)

print(dictionary)

df_ = pd.DataFrame(dictionary)
df_['rounded_Occur'] = round(df_['Occur'])


print(df_.head(50))
print(df_.tail(50))

total = df_.rounded_Occur.sum()

if total is True or total is not True:
    print(f"All numbers: {len(vals)}")
    print()
    print(f"Population Size: {n}")
    print(f"Sample Size: {total}")

    print()
    print(f'Population mean: {df["Income"].mean()}')

    dictionary_two = {
        'Sample Income': []
    }

    for i, ii in zip(df_['Income'], df_['rounded_Occur']):
        for num in range(int(ii)):
            dictionary_two['Sample Income'].append(i)

    df__ = pd.DataFrame(dictionary_two)
    s_mean = df__["Sample Income"].sum() / (df__["Sample Income"].count() - 1)
    print(f'Sample mean: {s_mean}')
    print(f"Hypothetical mean: {Hypothetical_Mean.mean}")

    df__['dev from mean'] = df__['Sample Income'] - s_mean
    df__['dev squared'] = df__['dev from mean'] ** 2

    print()
    pop_squared_sum = df['deviation sqrd'].sum()
    sam_squared_sum = df__['dev squared'].sum()

    print(f"Population dev squared +    : {pop_squared_sum}")
    print(f"    Sample dev squared +    : {sam_squared_sum}")

    print()
    sam_var = sam_squared_sum / df__['dev squared'].count()
    print(f'Pop Variance: {var}')
    print(f"Sample Variance: {sam_var}")

    print()
    print(f"Pop Standard Deviation: {sqrt(var)}")
    print(f'Sample Standard Deviation: {sqrt(sam_var)}')

# plt.hist(df['Income'])
# plt.show()