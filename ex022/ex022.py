'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiusculas

O nome com todas as letras maiusculas

Quantas letras ao todo.

Quantas letras tem o primeiro nome
'''

name = input('Enter your full name: ')

print(name.upper())
print(name.lower())
r = name.replace(' ','')
print(len(r))
split = name.split()
print(len(split[0]))


