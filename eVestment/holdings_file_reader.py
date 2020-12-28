import csv

filename = 'HoldingsTest.txt'
chunksize = 100000
i = 0
j = 1

holdings_list = []

with open(filename, newline='\n') as file_object:
    for line in file_object:
