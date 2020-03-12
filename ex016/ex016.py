# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n = float(input('Write any number on your wish: '))
x = trunc(n)
print('The integer part of your number {} is {}.'.format(n,x))
