#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
i = float(input('What is your income? '))
r = round(i+0.15*i,3)
print("Your income with 15% of raise is ${}.".format(r))
