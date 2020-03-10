#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('What is the price you want to discover the discount? '))
d = round(p-0.05*p,3)
print("The price with 5% off is ${}.".format(d))
