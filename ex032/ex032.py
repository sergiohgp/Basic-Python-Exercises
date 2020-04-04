'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        year = getYear()
        calcLeapYear(year)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getYear():
    year = float(input('Enter a year that you want to verify if is a leap year: '))
    return year

def calcLeapYear(year):
    if year == int(year):
        if year < 2019:
            if year%4 == 0 and year%100 != 0:
                print('{:.0f} was a leap year!'.format(year))
            elif year%100 == 0 and year%400 == 0:
                print('{:.0f} was a leap year!'.format(year))
            else:
                print('{:.0f} was not a leap year.'.format(year))
        elif year == 2019:
            print('2019 is not a leap year!')
        else:
            if year%4 == 0 and year%100 != 0:
                print('{:.0f} will be a leap year!'.format(year))
            elif year%100 == 0 and year%400 == 0:
                print('{:.0f} will be a leap year!'.format(year))
            else:
                print('{:.0f} will not be a leap year.'.format(year))
    else:
        print('The entered number is not a year')

main()

