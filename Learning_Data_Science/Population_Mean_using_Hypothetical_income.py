import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from random import randint
from math import sqrt

n = 100000
# np.linspace(1, 1000, 100, endpoint=True)
# randint(1, 500) for r in range(100)
# i for i in range(100
hold_it = sorted(randint(1, 100) for r in range(n))

dataframe = {
    'Income' : hold_it
}

df = pd.DataFrame(dataframe)


mean = df['Income'].mean()

if __name__ ==  '__main__':
    print()

df['deviation from mean'] = df['Income'] - mean

df['deviation from mean (abs)'] = abs(df['Income'] - mean)

df['deviation sqrd'] = df['deviation from mean (abs)'] ** 2

if __name__ ==  '__main__':
    print()
    print(df.head(50))
    print(df.tail(50))
    # print(df.head(50))
    # print(df.tail(50))

    print()

    print(f"Mean of Income Values: {mean}")

    print(f'Mean of negative deviations from the Income mean (supposed) : {df["deviation from mean"].iloc[0:50].mean()}')
    # print(f'Mean of first half of the data {df["Income"].iloc[0:50].mean()}')

    print(f'Mean of positive deviations from the Income mean (supposed) : +{df["deviation from mean"].iloc[50:100].mean()}')
    # print(f'Mean of second half of the data {df["Income"].iloc[50:100].mean()}')

    print(f"Sum of deviation squared : {df['deviation sqrd'].sum()}")

    print()
    print('Reason for similarity of the above mean(s): \n'
          'The total number of negative deviations from the Income mean almost always add up to the inverse of the total\n'
          'number of positive deviation from the Income mean')

    print()
    print(f"Sum of all deviations from the mean (non absolutes) : {df['deviation from mean'].sum()} . !! It should be equal "
          f"to zero")


    print()
    print(f"Mean of absolutes of all deviations from the mean {df['deviation from mean (abs)'].mean()} \n"
          f"This is similar to the above means as a result of that fact that values have only being scaled up twice!")

    print()
    print(f"Variance        : {df['Income'].var()}. ***WHY'S THIS ALWAYS LARGER THAN THE ONE BELOW THO!")

var = df['deviation sqrd'].sum() / df['deviation sqrd'].count()

if __name__ == '__main__':
    print(f"Variance_manual : {var}.\n"
          f"Note that data in the table have been approximated during the table creation process.")

    # print(sum(df['deviation from mean'].to_list()[0:50]) / df['deviation from mean'].count())

    print()
    std = sqrt(var)
    print(f"Standard Deviation       : {df['Income'].std()}")
    print(f"Standard Deviation_manual: {std}")

    print()
    print('VALUE COUNT')
    print((df['Income'].value_counts() / 100) * 10)

    print()
    print("UNDERSTANDING HOW ALL DEVIATIONS FROM THE MEAN CANCEL EACH OTHER OUT.")
    dataframe_two = {
        'deviation from mean_one' : df['deviation from mean'].iloc[0:50].to_list(),
        'deviation from mean_two' : df['deviation from mean'].iloc[50:100].to_list()[::-1]
    }

    new_df = pd.DataFrame(dataframe_two)

    new_df['difference'] = new_df['deviation from mean_one'] + new_df['deviation from mean_two']

    print(new_df.head(50))
    # print(new_df.tail(50))

    print(f'Sum of all negative values = {new_df["deviation from mean_one"].sum()} .The first column is assumed hold '
          f'negative values')
    print(f'Sum of all positive values = +{new_df["deviation from mean_two"].sum()} .The first column is assumed hold '
          f'negative values')
    print(f'sum difference = {new_df["difference"].sum()}')

    print()
    print('ANALYSING HYPOTHETICAL INCOME DATA')
    upto_100 = df[['Income']][df['Income'] < 101]['Income'].count()
    upto_200 = df[['Income']][df['Income'] < 201]['Income'].count() - upto_100
    upto_300 = df[['Income']][df['Income'] < 301]['Income'].count() - upto_200 - upto_100
    upto_400 = df[['Income']][df['Income'] < 401]['Income'].count() - upto_300 - upto_200 - upto_100
    upto_500 = df[['Income']][df['Income'] < 501]['Income'].count() - upto_400 - upto_300 - upto_200 - upto_100
    upto_600 = df[['Income']][df['Income'] < 601]['Income'].count() - upto_500 - upto_400 - upto_300 - upto_200 - upto_100
    upto_700 = df[['Income']][df['Income'] < 701]['Income'].count() - upto_600 - upto_500 - upto_400 - upto_300 - upto_200 \
               - upto_100
    upto_800 = df[['Income']][df['Income'] < 801]['Income'].count() - upto_700 - upto_600 - upto_500 - upto_400 - upto_300 \
               - upto_200 - upto_100
    upto_900 = df[['Income']][df['Income'] < 901]['Income'].count() - upto_800 - upto_700 - upto_600 - upto_500 - upto_400 \
               - upto_300 - upto_200 - upto_100
    upto_1000 = df[['Income']][df['Income'] < 1001]['Income'].count() - upto_900 - upto_800 - upto_700 - upto_600 \
                - upto_500 - upto_400 - upto_300 - upto_200 - upto_100

    dataframe_three = {
        'income' : np.linspace(100, 1000, 10),
        'Num of people earning this'  :   [upto_100, upto_200, upto_300, upto_400, upto_500, upto_600, upto_700,
                                                     upto_800, upto_900, upto_1000]
    }

    df_three = pd.DataFrame(dataframe_three)

    df_three['Total earnings'] = df_three['income'] * df_three['Num of people earning this']
    print(df_three)

    print()
    print('ANALYSING THE CUMMULATIVE POWER OF AN INCOME CLASS')

    def seg_power(income): # How much power does a income class have over others in terms of how many people it can acquire.
        income_index = df_three['income'].to_list().index(income)
        df_three['seg_power'] = df_three.iloc[income_index, 2]  / df_three['income']
        print(df_three)

    seg_power(500)

    # sns.barplot(df)
    # plt.show()

    # plt.boxplot(df['Income'])
    # plt.show()

