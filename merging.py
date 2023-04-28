import csv

dataset_1 = []
dataset_2 = []

with open("dwarf_stars.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("unit_converted_stars.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

headers_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
star_data_2 = dataset_2[1:]

headers = headers_1 + headers_2

star_data = []
for index,data_row in enumerate(star_data_1):
    star_data.append(star_data_1+ star_data_2)

with open("merged_dataset.csv", 'a+', newline  = '') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)