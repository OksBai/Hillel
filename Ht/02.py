import json

data = {
    123456: ('John', 30),
    234567: ('Alice', 25),
    345678: ('Bob', 35),
    456789: ('Emily', 28),
    567890: ('David', 40)
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("The dictionary was successfully written to the file 'data.json'.")
