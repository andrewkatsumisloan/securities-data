import pandas as pd
import numpy as np

from lib import JOINED_SP500_PATH
with open(JOINED_SP500_PATH, 'r') as f:
    joined_df = pd.read_csv(f, index_col=0)
    # joined_df = pd.read_csv(f, index_col=1)

    # Drop defaults to row
    joined_df = joined_df.drop(2)

    # Drop need to specify axis (1) in order to show intention to drop column
    joined_df = joined_df.drop('MMM', 1)

    # joined_df = joined_df.reset_index(drop=True, inplace=True)

    # del joined_df['Unnamed: 0']

joined_df = joined_df.head(10)
print(joined_df)

# Iterate over every cell.
for index, series in joined_df.iterrows():
    for column in joined_df.columns[1:]:
        joined_df.at[index, column] = 5

for column, series in joined_df.iteritems():
    for a, index in enumerate(series):
        joined_df.at[a, column] = 5

print('Modified', joined_df)

print(joined_df.loc[:, 'AAPL'])
print(joined_df)

# Use this to search by row.
print('This is loc', joined_df.loc[2])


# print(joined_df.loc(joined_df['AAPL']))

# Describe shows interesting features of
print(joined_df.describe())
describe_df = (joined_df.describe()).to_csv('describe.csv')


# Get row by index number


