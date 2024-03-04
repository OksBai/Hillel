import json
import csv
import random

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

operators = ['067', '066', '068', '093', '073', '097']

def generate_phone():
    if random.random() < 0.75:
        operator = random.choice(operators)
        number = ''.join(random.choices('0123456789', k=7))
        return f"{operator}{number}"
    else:
        return None

for key in data:
    data[key] = list(data[key]) + [generate_phone()]

with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ID', 'Name', 'Age', 'Phone number'])
    for key, value in data.items():
        writer.writerow([key] + list(value))

print("The data was successfully written to the file 'data.csv'.")
