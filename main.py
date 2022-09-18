from models import *


def addchickens(n, name):
    name.addNewTypeAnimal(Chicken())
    for i in range(n):
        name.addAnimal(Chicken())

def addcows(n, name):
    name.addNewTypeAnimal(Cow())
    for i in range(n):
        name.addAnimal(Cow())

def collectweeklyproduction(name):
    arr = []
    for i in range(7):
        arr.append(name.collectDailyProduction)
        print(arr)



if __name__ == "__main__":
    farm = Farm()
    addcows(10, farm)
    addchickens(20, farm)
    farm.getInfo()
    farm.collectDailyProduction()
    farm.collectWeeklyProduction()
    print(farm.arr)
