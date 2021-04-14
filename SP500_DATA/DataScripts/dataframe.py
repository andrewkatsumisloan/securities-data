import pickle
import pandas as pd
import os

from lib import JOINED_SP500_PATH, PICKLE_PATH


# Make a dataframe that contains the closing prices of all companies from the last 20 years.
def aggregate_data():
    # Opens the file containing the SP500 tickers list.
    with open(PICKLE_PATH, "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    # Numbers each ticker , iterates through number label and ticker.
    for count, ticker in enumerate(tickers):
        # For each ticker in SP500_Data folder set an index that is equal to the datetime column
        df = pd.read_csv('SP500_Data/Individual/{}.csv'.format(ticker))
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
    main_df.to_csv(JOINED_SP500_PATH)


def fix_datetime():
    with open(JOINED_SP500_PATH, 'r') as f:
        main_df = pd.read_csv(f)
        print(main_df)

    for count, date in enumerate(main_df['datetime']):
        data = date[:-9]
        main_df['datetime'][count] = data

    main_df.to_csv(JOINED_SP500_PATH)


if __name__ == '__main__':
    aggregate_data()
    fix_datetime()
