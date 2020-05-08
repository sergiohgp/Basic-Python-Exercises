from Car import *

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


#print(car2.displayCars())
#print(cl.displayInventory())
#print(c.salesMake('bmw'))
#print(c.salesYear(2019))
print(c.benefit(2019))


