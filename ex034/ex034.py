'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

def main():
    continueProgram = 'yes'
    while continueProgram == 'yes':
        income = getIncome()
        calcRaise(income)
        continueProgram = input('Dou want to continue the program? ')

def getIncome():
    income = float(input('Enter your monthly income: '))
    return income

def calcRaise(income):
    if income <= 1250:
        income = income*1.10
        print('You received a raise of 15%, your new salary is now ${:.2f}.'.format(income))
    else:
        income = income*1.15
        print('You received a raise of 10%, your new salary is now ${:.2f}.'.format(income))


main()