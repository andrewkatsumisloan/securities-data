import os

CODE_DIR = os.path.dirname(__file__)

JOINED_SP500_PATH = os.path.abspath(os.path.join(CODE_DIR, 'raw_data', 'aggregate_data', 'sp_joined_closes'))
print(JOINED_SP500_PATH)

PICKLE_PATH = os.path.abspath(os.path.join(CODE_DIR, 'sp500tickers.pickle'))
JSON_DATA_PATH = os.path.abspath(os.path.join(CODE_DIR, 'data.json'))
