import get_sp500_data
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sb

# Make a dataframe that contains the closing prices of all companies from the last 20 years.
def aggregate_data():
    # Opens the file containing the SP500 tickers list.
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    # Instantiate a main dataframe...
    main_df = pd.DataFrame()

    # Numbers each ticker , iterates through number label and ticker.
    for count, ticker in enumerate(tickers):
        # For each ticker in stock_data folder set an index that is equal to the datetime column
        df = pd.read_csv('stock_data/{}.csv'.format(ticker))
        df.set_index('datetime', inplace=True)
        df.rename(columns = {'close': ticker}, inplace=True)
        df.drop(['open', 'high', 'low', 'volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 1 == 0:
            print(count, ticker)

    # print(main_df.tail())
    main_df.to_csv('sp500_joined_closes.csv')


def fix_datetime():
    with open('sp500_joined_closes.csv', 'r') as f:
        main_df = pd.read_csv(f)
        print(main_df)
    for count, date in enumerate(main_df['datetime']):
        data = date[:-9]
        # print(data)
        main_df['datetime'][count] = data

    main_df.to_csv('sp500_joined_closes.csv')


if __name__ == '__main__':
    aggregate_data()
    fix_datetime()
    # graph_test('CSCO', 'UPS')
