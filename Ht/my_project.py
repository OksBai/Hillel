import csv

class Database:
    def __init__(self):
        self.data = []

    def load_from_file(self, filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                person = Person(*row)
                self.data.append(person)

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
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def age(self):
        if self.birth_date is None:
            return None
        if self.death_date:
            delta = self.death_date - self.birth_date
        else:
            from datetime import date
            delta = date.today() - self.birth_date
        return delta.days // 365

    def __str__(self):
        info = f'{self.name} {self.surname} {self.patronymic}'
        if self.birth_date:
            info += f', {self.age()} years, {self.gender}. was born {self.birth_date.strftime("%d.%m.%Y")}'
        if self.death_date:
            info += f'. died: {self.death_date.strftime("%d.%m.%Y")}'
        return info


def main():
    database = Database()
    while True:
        print("Menu:")
        print("1. download from file")
        print("2. save data in file")
        print("3. add new notice")
        print("4. search")
        print("5. exit")
        choice = input("choice the option: ")

        if choice == '1':
            filename = input("Enter the name for download: ")
            database.load_from_file(filename)
            print("data downloaded")
        elif choice == '2':
            filename = input("Enter the name for save: ")
            database.save_to_file(filename)
            print("data saved")
        elif choice == '3':
            name = input("enter your name: ")
            surname = input("enter your surname: ")
            patronymic = input("enter your father's name: ")
            birth_date = input("Enter the date of birth (format: dd.mm.yyyy): ")
            death_date = input("Enter the date of death (if applicable, format: dd.mm.yyyy): ")
            gender = input("Enter sex (m/f): ")
            person = Person(name, surname, patronymic, birth_date, death_date, gender)
            database.add_person(person)
            print("New notice added")
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



