import sqlalchemy as sa

import pandas as pd
import sqlalchemy as sa
import os

from dotenv import load_dotenv

load_dotenv(override=True)

RDS_HOST = os.getenv('RDS_HOST')
# print('This is the RDS_HOST: ', RDS_HOST)
METHOD = os.getenv('METHOD')
print('This is the ', METHOD, 'run of the model.')

engine = sa.create_engine(url=RDS_HOST)

DIST_PATH = os.path.abspath(os.path.join(__file__, '..', '..', 'data', 'puf', 'baseline_distributional_tables', '2016_dist_decile.csv'))

# Set USE_CACHE to false for
USE_CACHE = True


class SqlDb():
    def __init__(self):
        self.cache_dir = "/var/tmp/tagcache"
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def get_table(self, tablename):
        # if os.path.exists(os.path.join(self.cache_dir, tablename + '.csv')) and USE_CACHE:
        #     df = pd.read_csv(os.path.join(self.cache_dir, tablename + '.csv'))
        #     # print("Got table from cache: ", tablename)
        # else:
        df = pd.read_sql('SELECT * FROM "{}"'.format(tablename), con=engine)
        df.to_csv(os.path.join(self.cache_dir, tablename + '.csv'), index=False)
        return df

    def update_table(self, csv_path):
        """
        This takes a path to a local .csv and converts it to a SQL table.
        If the table already exists; updates the table. If the table doesn't exist, it adds the table.
        """
        df = pd.read_csv(csv_path)
        tablename = os.path.basename(csv_path)
        tablename = os.path.splitext(tablename)[0]
        print(tablename)

        df.to_sql(tablename,
                  engine,
                  index=False,
                  if_exists='replace',
                  chunksize=5000,
                  method=None)

    def delete_table(self, tablename):
        var = engine.execute('DROP TABLE "{}"'.format(tablename))


def get_csv(path, method=METHOD, float_precision=None):
    if method == 'csv':
        df = pd.read_csv(path, float_precision=float_precision)
        return df

    if method == 'sql':
        access = SqlDb()
        tablename = os.path.splitext(os.path.basename(path))[0]
        df = access.get_table(tablename)
        return df


if __name__ == '__main__':


    get_csv('/Users/AKS/TaxFoundation/tag/data/puf/baseline_pufs/puf_subsample/puf_subsample_3.csv', 'sql')
