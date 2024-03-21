import csv, datetime

class Database:
    def __init__(self):
        self.data = []

    def load_from_file(self, filename):
        "Returns True if file exists, else False"
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    person = Person(*row)
                    if person not in self.data:
                        self.data.append(person)
            return True
        except FileNotFoundError:
            return False

    def save_to_file(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for person in self.data:
                writer.writerow([person.name, person.surname, person.patronymic,
                                 person.birth_date, person.death_date, person.gender])

    def add_person(self, person):
        self.data.append(person)

    def search(self, query):
        results = []
        for person in self.data:
            if query.lower() in f'{person.name} {person.surname} {person.patronymic}'.lower():
                results.append(person)
        return results

class Person:
    def __init__(self, name=None, surname=None, patronymic=None, birth_date=None, death_date=None, gender=None):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        birth_date = birth_date.replace("/", ".")
        birth_date = birth_date.replace("-", ".")
        birth_date = birth_date.replace(" ", ".")
        self.birth_date = birth_date
        if death_date:
            death_date = death_date.replace("/", ".")
            death_date = death_date.replace("-", ".")
            death_date = death_date.replace(" ", ".")
        self.death_date = death_date
        self.gender = gender.lower()

    def age(self):
        """Returns age in whole years"""
        if self.birth_date is None:
            return 0
        start_date = datetime.datetime.strptime(self.birth_date, "%d.%m.%Y")
        end_date = None
        if self.death_date:
            end_date = datetime.datetime.strptime(self.death_date, "%d.%m.%Y")
        else:
            end_date = datetime.datetime.now()
        delta = end_date - start_date
        return delta.days // 365

    def __str__(self):
        info = f'{self.name} {self.surname} {self.patronymic}'
        if self.birth_date:
            info += f', {self.age()} years, {self.gender}. was born {self.birth_date}.'
        if self.death_date:
            info += f' died: {self.death_date}.'
        return info


def main():
    database = Database()
    while True:
        print("\nMenu:")
        print("1. load data from file")
        print("2. save data in file")
        print("3. add new person to database")
        print("4. search")
        print("5. exit")
        choice = input("Choose an option: ")

        if choice == '1':
            filename = input("Enter CSV filename to load from: ")
            if filename.lower().endswith(".csv"):
                did_load = database.load_from_file(filename)
                if did_load:
                    print("data downloaded")
                else:
                    print("file does not exist")
            else:
                print("filename must end with .csv")
        elif choice == '2':
            filename = input("Enter the CSV filename to save to: ")
            if filename.lower().endswith(".csv"):
                database.save_to_file(filename)
                print("data saved")
            else:
                print("filename must end with .csv")
        elif choice == '3':
            name = input("Enter person's given name: ")
            surname = input("Enter person's surname: ")
            patronymic = input("Enter person's father's name: ")
            birth_date = input("Enter the date of birth (format: dd.mm.yyyy): ")
            death_date = input("Enter the date of death (if applicable, format: dd.mm.yyyy): ")
            gender = input("Enter sex (m/f): ")
            person = Person(name, surname, patronymic, birth_date, death_date, gender)
            database.add_person(person)
            print("New record added")
        elif choice == '4':
            query = input("Enter data to search: ")
            results = database.search(query)
            if results:
                print("Search Results:")
                for result in results:
                    print(result)
            else:
                print("Nothing found.")
        elif choice == '5':
            print("bye!")
            break

main()
