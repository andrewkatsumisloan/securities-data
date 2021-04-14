import numpy as np
import pandas as pd
import pickle
from collections import Counter
from sklearn import svm, neighbors
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

# Labels: BUY, SELL, HOLD
def data_labels(ticker):
    days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)

    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0

def extract_featuresets(ticker):
    tickers, df = data_labels(ticker)
    # Map above function to dataframe
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]))

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))

    df.fillna(0, inplace=True)
    # Correct if/when goes from 0 to positive/negative int
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    # df.to_csv('labeltest.csv')

    del tickers[0]
    df_vals = df[[ticker for ticker in tickers]].pct_change()

    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)
    # df_vals.to_csv('asdfasdf.csv')

    # X featureset, y label
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values


    return X, y, df

def ml_operations(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # classifier = neighbors.KNeighborsClassifier()
    classifier = VotingClassifier([('linearsvc', svm.LinearSVC()), ('randforest', RandomForestClassifier()), ('knearest', neighbors.KNeighborsClassifier())])
    classifier.fit(X_train, y_train)

    confidence = classifier.score(X_test, y_test)
    print('Accuracy', confidence)
    predictions = classifier.predict(X_test)

    print('Predicted spread', Counter(predictions))


    return confidence


ml_operations('CVX')


# data_labels('AAPL')