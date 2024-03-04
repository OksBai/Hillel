import json

data = {
    123456: ('Alla', 30),
    234567: ('Vasyl', 25),
    345678: ('Iryna', 35),
    456789: ('Anastasiia', 28),
    567890: ('Mykolay', 40)
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("The dictionary was successfully written to the file 'data.json'.")
