import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Correlation table

def correlation(list):
    '''
    Creates a correlation table from a given list of SP500 companies.
    :param list: List containing ticker symbols as strings
    :return: correlation table with heatmap
    '''
    with open('sp500_joined_closes.csv') as f:
        main_df = pd.read_csv(f)
        # print(main_df)
        df = pd.DataFrame()

        for a in range(len(list)):
            array = main_df[list[a]].values
            df['{}'.format(list[a])] = array

        corr_table = df.corr()
        print(corr_table)

        sns.heatmap(corr_table, annot=True, annot_kws={"size":8})
        plt.show()

        # first = main_df[ticker]
        # print(df)



correlation(['AAPL', 'MSFT', 'GE', 'IBM', 'BA'])

