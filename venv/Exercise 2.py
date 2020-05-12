import csv
with open("100 Sales Records.csv") as opened_file:
    read_file = csv.reader(opened_file)
    data = list(read_file)


new_list_list = []

for row in data:
    region = row[0]
    country = row[1]
    total_profit = row[-1]
    list_3 = [region, country, total_profit]
    new_list_list.append(list_3)

for row in new_list_list:
    print(row)

with open("Summary list data.csv", "w", newline = "") as opened_file:
    written_file = csv.writer(opened_file)
    written_file.writerows(new_list_list)