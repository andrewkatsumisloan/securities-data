import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""
Known issues: date mismatch on plotting
"""

def graph_test_compare(list):
    with open('sp500_joined_closes.csv', 'r') as f:
        tick_df = pd.read_csv(f)
        y_axes = []
        for a in range(len(list)):
            # print(tick_df['{}'.format(list[a])].values)
            y_axes.append(tick_df['{}'.format(list[a])].values.tolist())


    fig, ax = plt.subplots()

    # abc = [[1,2,4]]
    # abc.append([5, 4, 2])
    # print(abc)

    x_axis = tick_df['datetime'].values.tolist()
    # y_axis = tick_df['ticker']
    plt.style.use('seaborn')
    ax.set_xlabel('Time since 2000 (Years)')
    ax.set_ylabel('Stock Price ($USD)')
    # ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    # ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))

    for i in range(len(y_axes)):
        ax.plot(x_axis, y_axes[i], label='{}'.format(list[i]), linewidth=0.65)

    # print(y_axis1)
    ax.xaxis.set_major_locator(mdates.YearLocator(2, month=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    plt.legend()
    plt.show()

def graph_with_dma(ticker, window):
    """
    This function takes (1) ticker and a integer and plots the price history of ticker
    with [window]-day moving average superimposed.
    :param ticker: String, ticker symbol for given SP500 company
    :param window: x-Day Moving Average
    :return:
    """
    with open('sp500_joined_closes.csv', 'r') as f:
        tick_df = pd.read_csv(f)
        price_hist = tick_df['{}'.format(ticker)]

    fig, ax = plt.subplots()
    x_axis = tick_df['datetime']

    rolling_average = tick_df['{}'.format(ticker)].rolling(int(('{}'.format(window)))).mean()

    ax.set_title('20 Year Price Data for {}'.format(ticker))
    ax.set_xlabel('Time since 2000 (Years)')
    ax.set_ylabel('Stock Price ($USD)')

    ax.plot(x_axis, price_hist, label='{}'.format(ticker))
    ax.plot(x_axis, rolling_average, label='{} Day Moving Average'.format(window))

    ax.xaxis.set_major_locator(mdates.YearLocator(2, month=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    plt.style.use('seaborn')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    graph_test_compare(['CSCO', 'UPS', 'AAPL', 'GE', 'MSFT', 'IBM', 'BA', 'CVX'])
    graph_with_dma('AAPL', 55)
