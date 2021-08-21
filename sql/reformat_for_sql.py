import re


from lib import JOINED_SP500_PATH

handle = open(JOINED_SP500_PATH, 'r')
lines = handle.readlines()
handle.close()

handle = open('sql_format.csv', 'w')
handle.write('ticker,date_time,closing_price\n')

tickers = re.split(',', lines[0].rstrip())[2:]

for line in lines[1:]:
    larray = re.split(',', line.rstrip())
    date = larray[1]
    prices = larray[2:]
    for i in range(len(prices)):
        if prices[i]:
            handle.write('{0},{1},{2}\n'.format(tickers[i], date, prices[i]))

handle.close()
