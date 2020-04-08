'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

def main():
    continueProgram = 'y'
    while continueProgram == 'y':
        hp = getHousePrice()
        income = getIncome()
        years = getYears()
        finance = calcFinance(hp, years)
        percent = calcIncome(income)
        allowedDenied(finance, percent)
        continueProgram = input('Dou want to continue the program?(Enter y for yes and n for no): ')

def getHousePrice():
    hp = int(input('Enter the house\'s price: '))
    return hp

def getIncome():
    income = int(input('Enter your monthly income: '))
    return income

def getYears():
    years = int(input('Enter the number of years you want to finance the house: '))
    return years

def calcFinance(hp, years):
    months = years*12
    finance = hp/months
    return finance

def calcIncome(income):
    percent = income*.30
    return percent

def allowedDenied(finance, percent):
    if finance <= percent:
        print('Congratulations!! Your finance was approved!'
              'You will pay ${:.2f}/month.'.format(finance))
    else:
        print('Sorry, your finance was denied. '
              'You have to pay ${:.2f}/month and it\'s greater then 30% of yor income.'.format(finance))

main()