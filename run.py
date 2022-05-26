import csv
import json


filename_csv = 'test_task_data.csv'
filename_json = 'test.json'


file_cvs = open(filename_csv, 'r')
csv_reader = csv.DictReader(file_cvs)
data =[]

for row in csv_reader:
    d = {'data': row['date'], 'campaign':  row['campaign'], 'clicks': row['clicks']}
    data.append(d)

record = {'data': data}
for i in range(len(data)):
    file_json = open(filename_json, 'w')
    json.dump(record, file_json)


