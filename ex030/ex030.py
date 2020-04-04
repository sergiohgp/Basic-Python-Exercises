'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        n = getNumber()
        oddEven(n)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getNumber():
    n = int(input('Enter an integer number: '))
    return n

def oddEven(n):
    if n%2 != 0:
        print('{} is an odd number!'.format(n))
    else:
        print('{} is an even number!'.format(n))

main()