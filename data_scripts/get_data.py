import sys
import pickle
import os
import bs4 as bs
import json
import pandas as pd
import requests
import math
import time

sys.path.append('../')
from lib import PICKLE_PATH, JSON_DATA_PATH


key = 'RFJECPTJLRRH42GDRRFPUBVA7ODHJZON'

# price_hist_endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format('FB')
# price_hist_endpoint = 'https://api.tdameritrade.com/v1/marketdata/FB/pricehistory'


# Make more concise later
current_time = math.floor(time.time()*1000)

payload = {
    'apikey': key,
    'periodType': 'year',
    'frequencyType': 'daily',
    'frequency': '1',
    'endDate': current_time,
    'startDate': '946719000000',
    'needExtendedHoursData': 'false'
}


def list_tickers():
    with open(PICKLE_PATH, "rb") as f:
        tickers = pickle.load(f)
    return tickers


# This scrapes the wikipedia for the SP500 using beautiful soup,
def sp500_ticker_list():
    resp = requests.get(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    # print(soup.text)
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    # From the first row onward...
    for row in table.findAll('tr')[1:]:
        # Get the first element in each row.
        ticker = row.findAll('td')[0].text
        ticker = ticker[:-1]
        tickers.append(ticker)
    # Save the sp500 tickers wb = write bits
    with open(PICKLE_PATH, "wb") as f:
        pickle.dump(tickers, f)
    # print(tickers)
    return tickers


def get_data_tda(reload_sp500=False):
    if reload_sp500:
        tickers = sp500_ticker_list()
    else:
        # rb = read bytes
        with open(PICKLE_PATH, "rb") as f:
            tickers = pickle.load(f)
        # If this directory does not exist, create it.

        # print(tickers)
        # For each ticker, if the path does not exist for their historical data file...
        for ticker in tickers:
            # if not os.path.exists('sp500_data/{}'.format(ticker)):
            #     pass
            print(ticker)
            # Get the desired endpoint (ticker specific)
            endpt = format_request(ticker)

            # Request data according to parameters and endpoint.  Store response in content.
            content = requests.get(url=endpt, params=payload)

            # Convert the data to dictionary format.
            data1 = (content.json()).get('candles')
            # print(content.json())

            # while not data1:
            #     data1 = (content.json()).get('candles')
            #
            #     print('failed to get candles from', ticker)

            # Dump the data
            with open(JSON_DATA_PATH, 'w') as outfile:
                json.dump(data1, outfile)
            # print(data1)

            df = pd.read_json(JSON_DATA_PATH)

            df.to_csv('../raw_data/individual/{}.csv'.format(ticker), index=False)


def format_request(ticker):
    price_hist_endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(
        ticker)
    return price_hist_endpoint


if __name__ == '__main__':
    sp500_ticker_list()
    get_data_tda()



# Improvements
# Since companies in the SP500 are constantly changing (as companies are delisted and added to the index)
# it makes sense to run th sp500_ticker_list() before each call to update the local data.


# Ideas
# Make a command line tool that allows you to request any DMA from a given ticker


