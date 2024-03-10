class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = self.is_valid_fuel_type(fuel_type)
        Car.NUMBER_OF_CARS += 1
        self.number = Car.NUMBER_OF_CARS

        if color not in Car.COLORS:
            Car.COLORS.append(color)

    def __str__(self):
        return f"{self.model} – {self.year} – {self.fuel_type} - {self.color}"

    def is_valid_fuel_type(self, fuel_type):
        return fuel_type if fuel_type in Car.FUEL_TYPES else Car.FUEL_TYPES[0]

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS

    @property
    def numbers(self):
        return f"{self.number} from {Car.NUMBER_OF_CARS}"

car_1 = Car('Zaz', 1979, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'red')
car_3 = Car('VOLVO', 2012, 'електрика', 'black')
car_4 = Car('Mersedes', 2012, 'гібрид', 'black')

print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
