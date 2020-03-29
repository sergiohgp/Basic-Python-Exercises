'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random

def main():
    endProgram = 'no'
    while endProgram == 'no':
        num = getNumber()
        guess(num)
        endProgram = input('Do you want to end the program? (Enter either yes or no only): ')

def getNumber():
    num = random.randint(0,5)
    return num

def guess(num):
    guess = int(input('Enter an integer guess between 0 and 5: '))
    while guess != num:
        if guess > num:
            print('{} is higher then the right number, please try again: '.format(guess))
            guess = int(input('Enter another integer number between 0 and 5: '))
        elif guess < num:
            print('{} is lower then the right number, please try again: '.format(guess))
            guess = int(input('Enter another integer number between 0 and 5: '))
    else:
        print('Correct!!! You won!!')
main()