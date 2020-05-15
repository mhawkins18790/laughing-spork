import csv

index_num = 1

with open('banklist.csv') as csvfile:
    bank_name = csv.DictReader(csvfile)
    for row in bank_name:
        if row['ST'] == 'CA':
            print(str(index_num) + "). " +
                  row['Bank Name'] + " " + row['City'] + " " + row['ST'])
            index_num = index_num + 1
