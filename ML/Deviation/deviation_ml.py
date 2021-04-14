import pandas as pd
import numpy as np
import pickle

with open('../../sp500tickers.pickle', 'rb') as f:
    tickers = pickle.load(f)


def find_spike(array):
    '''
    This identifies all of the spikes in the time series pricing data for a single security and returns index/datetime
    :param array: d
    :return: 
    '''
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    df.fillna(0, inplace=True)
    print(df)


def df_normalized(dataframe):
    '''
    This creates a dataframe of normalized % change data
    :return: Modified dataframe
    '''
    pass


def spike_index(ticker):
    '''
    Returns the index of all +/- 3.5% spikes for a given ticker
    '''
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    df.fillna(0, inplace=True)
    series = df[ticker].values.tolist()
    print(len(series))
    # series = [x for x in series if x > 0]

    norm = []
    for count, i in enumerate(series):
        # print(count)
        if count == 0:
            pass
        else:
            if series[count] > 0:
                norm.append((series[count]-series[count-1])/(series[count]))
                # print((series[count]-series[count-1])/(series[count]))
            else:
                norm.append(0)

    # spikes = [(i, x) for i, x in enumerate(norm) if math.fabs(x) > 0.05]
    print('This is len norm', len(norm))
    norm = np.array(norm)
    print('This is np len norm', len(norm))

    return norm


def spike_dataframe(tickers):
    with open('sp500tickers.pickle', 'rb') as f:
        t_list = pickle.load(f)
    # print(t_list)
    norm_df = pd.DataFrame()
    for count, i in enumerate(t_list):
        print(1, t_list[count])
        a = spike_index(t_list[count])
        norm_df['{}'.format(t_list[count])] = a
    norm_df.to_csv('norm_df.csv')


# df_normalized(pd)
spike_index('AAPL')
spike_dataframe('a')
