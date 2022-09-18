import random


class Animal:
    index = 1
    animalId = 0

    def collectProduct(self):
        pass

    def getName(self):
        pass


class Cow(Animal):
    def __init__(self):
        self.animalId = Animal.index
        Animal.index += 1
        self.product = "Молоко"

    def getName(self):
        return "Корова"

    def collectProduct(self):
        return random.randint(8, 12)


class Chicken(Animal):
    def __init__(self):
        self.animalId = Animal.index
        Animal.index += 1
        self.name = "Курица"
        self.product = "Яйцо"

    def getName(self):
        return self.name

    def collectProduct(self):
        return random.randint(0, 1)


class Farm:
    def __init__(self):
        self.yard = {}
        self.dailyproduction = {}
        self.weeklyproduction = {}

    def addNewTypeAnimal(self, animal):
        self.yard[type(animal).__name__] = []

    def addAnimal(self, animal):
        self.yard[type(animal).__name__].append(animal)

    def getInfo(self):
        for item in self.yard:
            print(f"Всего {len(self.yard[item])} {item}")

    def collectProduction(self):
        for i in range(7):
            for animal in self.yard:
                sum = 0
                type = self.yard[animal][0].product
                self.dailyproduction[type] = sum
                for item in self.yard[animal]:
                    sum += item.collectProduct()
                self.dailyproduction[type] += sum

