from Car import *

class Car:
   def __init__(self, make, model, year, pur_price, pur_date, sold_price, sold_date):
      self.make = make
      self.model = model
      self.year = year
      self.pur_price = pur_price
      self.pur_date = pur_date
      self.sold_price = sold_price
      self.sold_date = sold_date
      self.sold_on = False

   def sell(self):
      if self.sold_on == True:
         print('This item has been sold')
      else:
         self.sold_on = True

   def sale_price(self):
      if self.sold_on:
         return 0.0
      return self.sold_price

   def purchase_price(self):
      return self.flat_rate - (0.10 * self.miles)

class Cars(Car, object):
   def __init__(self, wheels, miles, make, model, year, gear, color):
      super(Car, self).__init__(wheels, miles, make, model, year)
      self.gear = gear
      self.color = color
      self.flat_rate = 7500
   def getDescription(self):
      sale_price = self.sale_price()
      return '{} {} {} - {}, {} miles >>> ${}'.format(self.make, self.model, self.year, self.color, self.miles, sale_price)

class Truck(Car, object):
   def __init__(self, wheels, miles, make, model, year, seats):
      super(Truck, self).__init__(wheels, miles, make, model, year)
      self.seats = seats
      self.flat_rate = 9000

   def sale_price(self):
      if self.sold_on:
         return 0.0
      return 4000

   def getDescription(self):
      sale_price = self.sale_price()
      return '{} {} {}, {} miles - {} seats >>> ${}'.format(self.make, self.model, self.year, self.miles, self.seats, sale_price)