import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

sys.path.append('./')
from lib import JOINED_SP500_PATH

# Correlation table
def correlation(list):
    """
    Creates a correlation table from a given list of SP500 companies.
    :param list: List containing ticker symbols as strings
    :return: correlation table with heatmap
    """
    with open(JOINED_SP500_PATH) as f:
        main_df = pd.read_csv(f)
        # print(main_df)
        df = pd.DataFrame()

        for a in range(len(list)):
            array = main_df[list[a]].values
            df['{}'.format(list[a])] = array

        # corr_table = df.corr().to_dict()
        corr_table = df.corr()
        
        # print(corr_table)
        # print(type(corr_table))

        print('This is the columns: ', corr_table.columns)
        ret_list = []
        for x in corr_table: 
            ret_list.append(corr_table[x].tolist())
            # print(corr_table[x])
        
        for x in ret_list: 
            pass

        ret_list.insert(0, corr_table.columns.tolist())
        print(ret_list)

        sns.heatmap(corr_table, annot=True, annot_kws={"size":8})
        plt.savefig('./corr_heatmap.png')

        plt.show()


correlation(['AAPL', 'MSFT', 'GM'])