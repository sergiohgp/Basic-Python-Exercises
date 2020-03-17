#Faca um programa que ajude um professor a selecionar randomicamente um dos quatro alunos para apagar o quadro.
import random
a1 = str(input("Student one's name: "))
a2 = str(input("Student two's name: "))
a3 = str(input("Student three's name: "))
a4 = str(input("Student four's name: "))
x = random.randint(1, 4)

if x == 1:
    print('The chosen one is {}!'.format(a1))
if x == 2:
    print('The chosen one is {}!'.format(a2))
if x == 3:
    print('The chosen one is {}!'.format(a3))
if x == 4:
    print('The chosen one is {}!'.format(a4))
