import time
class Auto:
    def __init__(self, brand, age, mark, color="black", weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="black", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="black", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")

truck1 = Truck("Volvo", 8, "XZ", 3000)
truck2 = Truck("MAN", 9, "Some", 2500, color="blue")

car1 = Car("Toyota", 4, "Corolla", 220)
car2 = Car("BMW", 7, "M3", 280, color="white")

truck1.move()
truck1.load()

car2.move()

