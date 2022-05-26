import csv
import json
import textwrap

filename_csv = 'test_task_data.csv'
filename_json = 'test.json'

data =[]
with open(filename_csv, 'r') as file_cvs:
    csv_reader = csv.DictReader(file_cvs)
    for row in csv_reader:
        d = {'data': row['date'], 'campaign':  row['campaign'], 'clicks': row['clicks']}
        data.append(d)

record = {'data': data}

with open(filename_json, 'w') as file_json:
    json.dump(record, file_json)







