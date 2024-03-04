class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = "black"
        self.weight = 0

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")
