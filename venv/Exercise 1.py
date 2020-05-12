#opened_file = open("employees.csv")
#import csv
#read_file = csv.reader(opened_file)
#dataset = list(read_file)

#print(dataset)

import csv
with open("100 Sales Records.csv") as opened_file:
#opened_file = open("100 Sales Records.csv")
#import csv
    read_file = csv.reader(opened_file)
    data = list(read_file)


counter_europe = 0
total_amount_units = 0
list_types = []
for row in data[1:]:
    if row[0] == "Europe":
        counter_europe += 1

    total_amount_units += int(row[8])

    if row[2] in list_types:
        pass
    else:
        list_types.append(row[2])

print("Number of records from Europe is ", counter_europe)
print("Total amount of units sold is ", total_amount_units)
print(list_types)