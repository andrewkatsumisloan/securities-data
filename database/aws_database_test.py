import sys
import os
import pandas as pd
import sqlalchemy as sa


sys.path.append('../')
from data_scripts.get_data import sp500_ticker_list

from dotenv import load_dotenv

load_dotenv(override=True)

RDS_HOST = os.getenv('RDS_HOST')
print('This is the RDS_HOST: ', RDS_HOST)

current_dir = os.path.dirname(__file__)
directory_path = os.path.join(current_dir, '..', 'raw_data', 'individual')

engine = sa.create_engine(url=RDS_HOST)

class db_access():
    def get_table(self, tablename):
        df = pd.read_sql('SELECT * FROM "{}"'.format(tablename), con=engine)
        return df

    def update_table(self, directory_path):
        """
        This takes a path to a local .csv and converts it to a SQL table.
        If the table already exists; updates the table. If the table doesn't exist, it adds the table.
        """
        for file in os.listdir(directory_path):
            print(file)
            # file_path = file
            # print(directory_path + '/{0}'.format(file))
            df = pd.read_csv(directory_path + '/{0}'.format(file))
            tablename = os.path.basename(directory_path + '/{0}'.format(file))
            tablename = os.path.splitext(tablename)[0]
            print(tablename)

            df.to_sql(tablename,
                      engine,
                      index=False,
                      if_exists='replace',
                      chunksize=5000,
                      method=None)

    def update_all(self): 
        ticker_list = sp500_ticker_list()
        print(ticker_list)
        for ticker in ticker_list:
            df = pd.read_csv('../raw_data/individual/{0}.csv'.format(ticker)) 
            df.to_sql(ticker,
                      engine,
                      index=False,
                      if_exists='replace',
                      chunksize=5000,
                      method=None)
            print('{0} '.format(ticker), 'updated presumably.')
        
        return

    def delete_table(self, tablename):
        var = engine.execute('DROP TABLE "{}"'.format(tablename))


def get_csv(ticker, float_precision=None):
        access = db_access()
        df = access.get_table(ticker)
        return df


if __name__ == '__main__':
    access = db_access()
    # access.update_table(directory_path)
    print(get_csv('MMM'))
    # access.update_all()
    pass