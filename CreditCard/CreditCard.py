class CreditCard:

    #constructor
    #init = initializer
    def __init__(self, name, number, balance, limit):  #atributes of the class
        self.cname = name
        self.cnumber = number
        self.cbalance = balance
        self.climit = limit


    def swipe(self, amount):
        if (self.cbalance + amount) <= self.climit:
            self.cbalance = self.cbalance + amount
            print('New Balance is {}.'.format(self.cbalance))
        else:
            x = self.climit - self.cbalance
            print('You exceeded the limit in ${}.'.format(x))

    def payBill(self, amount):
        self.cbalance = self.cbalance - amount

    def getBalance(self):   #a getter or accessor function
        return self.cbalance

    def setLimit(self, newLimit):  #a setter or a mutator function
        self.climit = newLimit







    #using the class
card1 = CreditCard("Adam", "123456789", 0, 1000)
card2 = CreditCard("Jack", "123456756", 0, 2000)

#print (card1.cname)


card1.swipe(500)
card1.swipe(1200)
#print(str(card1.cbalance))
#card1.payBill(300)

#print(str(card1.cbalance))