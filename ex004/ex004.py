#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
x = input('Write something... ')
print(type(x))
print('what you have typed is alphanumeric?',x.isalnum())
print('what you have typed is a number?', x.isnumeric())
print('what you have typed is a alpha?',x.isalpha())
print('what you have typed is a space?',x.isspace())
