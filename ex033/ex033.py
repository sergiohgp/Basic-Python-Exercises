'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        n1 = getNumbers()
        n2 = getNumbers()
        n3 = getNumbers()
        calcGreatest(n1, n2, n3)
        calcLowest(n1, n2, n3)
        endProgram = input('Do you want to end this program?')

def getNumbers():
    n = float(input('Enter one number: '))
    return n

def calcGreatest(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print('{} is the greatest number!'.format(n1))
    elif n2 > n1 and n2 > n3:
        print('{} is the greatest number!'.format(n2))
    else:
        print('{} is the greatest number!'.format(n3))

def calcLowest(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        print('{} is the lowest number!'.format(n1))
    elif n2 < n1 and n2 < n3:
        print('{} is the lowest number!'.format(n2))
    else:
        print('{} is the lowest number!'.format(n3))



main()