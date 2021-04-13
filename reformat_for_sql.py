import re

handle = open('sp500_joined_closes.csv', 'r')

lines = handle.readlines()
handle.close()

handle = open('SQL_formatted.csv', 'w')
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


# COPY SP500Data(ticker, date_time, closing_price)
# FROM '/Users/AKS/FinancialData/SQL_formatted.csv'
# DELIMITER ',';
#
#
# INSERT INTO SP500Data (ticker, date_time, closing_price) VALUES ('AAPL', 2000-01-03, 42.4)
#
# INSERT INTO "public"."SP500Data" (ticker, date_time, closing_price) VALUES ("AAPL", 2000-01-03, 42.4)
#
# COPY "public"."SP500Data" (ticker, date_time, closing_price)
# FROM '/Users/AKS/FinancialData/SQL_formatted.csv'
# DELIMITER ',' CSV HEADER;
