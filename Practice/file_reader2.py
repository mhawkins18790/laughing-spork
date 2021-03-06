import csv

filename = 'HoldingsTest.txt'
holdings_list = []

with open(filename, newline='\n') as holdings:
    holdings_reader = csv.DictReader(holdings, delimiter='|')
    for holding in holdings_reader:
        holdings_list.append(dict(holding))


time_period_2008 = []

for holding in holdings_list:
    if holding['Year'] == '2008':
        time_period_2008.append(dict(holding))


for time in time_period_2008:
    print(time)
