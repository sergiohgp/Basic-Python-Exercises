import datetime as d
from time import sleep

class Car:
    num_of_cars = 0

    def __init__(self, make, model, pur_price, pur_date, sold_price, sold_date):
        self.__make = make
        self.__model = model
        self.__pur_price = pur_price
        self.__pur_date = pur_date
        self.__sold_price = sold_price
        self.__sold_date = sold_date

        Car.num_of_cars += 1

    def getMake(self):
        return self.__make

    def setMake(self, make):
        self.__make = make

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model

    def getPurchasePrice(self):
        return self.__pur_price

    def setPurchasePrice(self, pur_price):
        self.__pur_price = pur_price

    def getPurchaseDate(self):
        return self.__pur_date

    def setPurchaseDate(self, pur_date):
        self.__pur_date = pur_date

    def getSoldPrice(self):
        return self.__sold_price

    def setSoldPrice(self, sold_price):
        self.__sold_price = sold_price

    def getSoldDate(self):
        return self.__sold_date

    def setSoldDate(self, sold_date):
        self.__sold_price = sold_date

    def displayCars(self):
        result = f'Make: {self.__make}\n'
        result += f'Model: {self.__model}\n'
        result += f'Purchase Price: {self.__pur_price}\n'
        result += "Purchase Date:" + self.__pur_date.strftime('%x') + '\n '
        result += f'Sold Price: {self.__sold_price}\n'
        result += "Sold Date:" + self.__sold_date.strftime('%x') + '\n '
        result += '-'*50
        return result

class Collection:

    def __init__(self):
        self.__inventory = []

    def add_car(self, newcar):
        if newcar not in self.__inventory:
            self.__inventory.append(newcar)

    def remove_car(self, newcar):
            self.__inventory.remove(newcar)

    def displayInventory(self):
        print('List of cars in the inventory:')
        for c in self.__inventory:
            if c in self.__inventory:
                print(c.displayCars())
                sleep(.5)

    def array(self):
        return self.__inventory

class Count:

    def __init__(self):
        self.collection = Collection()

    def salesYear(self, y):
        array = self.collection.array()
        counter = 0
        for c in array:
            if int(c.getSoldDate().year) == y:
                counter += 1
        return counter


    def salesMake(self, m):
        array = self.collection.array()
        counter = 0
        for c in array:
            if c.getMake() == m:
                counter += 1
        return counter

    def benefit(self, y):
        array = self.collection.array()
        total = 0
        pur = 0
        benefit = 0
        for c in array:
            if int(c.getSoldDate().year) == y:
                total += c.getSoldPrice()
                pur += c.getPurchasePrice()
                benefit = total - pur
        return benefit


car1 = Car('vw', 'jetta', 12000, d.date(2018, 11, 23), 20000, d.date(2019, 11, 14))
car2 = Car('bmw', 'x2', 40000, d.date(2019, 4, 15), 39000, d.date(2019, 5, 15))
car3 = Car('kia', 'forte', 22000, d.date(2019, 5, 14), 25000, d.date(2019, 8, 14))
car4 = Car('kia', 'optima', 14000, d.date(2018, 12, 9), 19000, d.date(2019, 11, 14))
car5 = Car('mercedes', 'c43', 19000, d.date(2019, 9, 3), 28000, d.date(2019, 11, 14))

c = Count()
cl = c.collection

cl.add_car(car1)
cl.add_car(car2)
cl.add_car(car3)
cl.add_car(car4)
cl.add_car(car5)

a = Car.num_of_cars
#print(a)


#print(car2.displayCars())
#cl.displayInventory()
#print(c.salesMake('bmw'))
#print(c.salesYear(2019))
#print(c.benefit(2019))












