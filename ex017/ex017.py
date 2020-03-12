#Faca um programa que leia os catetos de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Write the measure of the first catetum: '))
ca = float(input('Write the measure of the second catetum: '))
h = math.sqrt((co**2)+(ca**2))
print('The hipothenuse is {}'.format(h))
