import requests
import datetime
import pandas as pd
import json
import bs4 as bs
import os
import pickle

key = 'RFJECPTJLRRH42GDRRFPUBVA7ODHJZON'

# price_hist_endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format('FB')
# price_hist_endpoint = 'https://api.tdameritrade.com/v1/marketdata/FB/pricehistory'

payload = {
    'apikey': key,
    'periodType': 'year',
    'frequencyType': 'daily',
    'frequency': '1',
    'endDate': '1618286676000',
    'startDate': '946719000000',
    'needExtendedHoursData': 'false'
}


def list_tickers():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
    return tickers


# This scrapes the wikipedia for the SP500 using beautiful soup,
def sp500_ticker_list():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
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
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    print(tickers)
    return tickers


def get_data_tda(reload_sp500=False):
    if reload_sp500:
        tickers = sp500_ticker_list()
    else:
        # rb = read bytes
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
        # If this directory does not exist, create it.
        if not os.path.exists('sp500_data'):
            os.makedirs('sp500_data')

        # For each ticker, if the path does not exist for their historical data file...
        for ticker in tickers:
        # for ticker in ['FCX']:
            # if not os.path.exists('sp500_data/{}'.format(ticker)):
            #     ret_payl()
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
            with open('data.json', 'w') as outfile:
                json.dump(data1, outfile)
            # print(data)

            df = pd.read_json('data.json')

            df.to_csv('SP500_Data/Individual/{}.csv'.format(ticker), index=False)



def format_request(ticker):
    price_hist_endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(ticker)
    return price_hist_endpoint


if __name__ == '__main__':
    sp500_ticker_list()
    get_data_tda()


# Time in seconds not milliseconds from epoch to datetime format

# print(datetime.datetime.fromtimestamp(1593580828).strftime('%c'))

# PrettyPrint
# pp = pprint.PrettyPrinter()
# pp.pprint(data)

# Ideas
# Make a command line tool that allows you to request any DMA from a given ticker


''' 
def ret_payl():
    payload = {
        'apikey': key,
        'periodType': 'year',
        # 'period': '20',
        'frequencyType': 'daily',
        'frequency': '1',
        'endDate': '1605583258000',
        'startDate': '946719000000',
        'needExtendedHoursData': 'false'
    }
    return payload
'''


