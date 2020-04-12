'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
'''

print('==========_________Desafio 038__________==========')
print('')
from time import sleep

n1 = int(input('\033[1mDigite o primeiro numero: '))
n2 = int(input('\033[1mDigite o segundo numero: '))
print('\033[1;31mCalculando a resposta...\033[m')
sleep(1.5)
if n1 > n2:
    print('\033[1mO maior numero é \033[1;34m{} \033[m'.format(n1))
    print('\033[1mO menor é \033[1;31m{} \033[m'.format(n2))
elif n2 > n1:
    print('\033[1mO maior é \033[1;34m{} \033[m'.format(n2))
    print('\033[1mO menor numero é \033[1;31m{}'.format(n1))
else:
    print('\033[4;33mOs numeros são iguais.')

print('\033[42m'+'\033[1m'+'\033[33m'+'Isto eh amarelo negrito com fundo verde'+'\033[0;0m')
