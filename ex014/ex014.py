#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
n = float(input('What is the temperature in Celcius now? '))
f = round(n*9/5+32,2)
print("The same temperature, in Fahrenheit, is {}.".format(f))
