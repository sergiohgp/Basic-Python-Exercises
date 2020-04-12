'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        yearOfBirth = getDOB()
        calcAge(yearOfBirth)
        endProgram = input('Do you want to end the program? (Enter y for yes and n for no): ')

def getDOB():
    yearOfBirth = int(input('Enter the year you were born: '))
    return yearOfBirth

def calcAge(yearOfBirth):
    age = 2019 - yearOfBirth
    if age == 18:
        print('This is the exactly year to list your name in military...What are you waiting for?')
    elif age < 18:
        print('You are too young to to list in military, wait for more {} years.'.format(18-age))
    else:
        print('You passed the time to list in military, you are {} years late.'.format(age-18))


main()