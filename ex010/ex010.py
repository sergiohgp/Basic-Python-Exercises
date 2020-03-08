#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
d = float(input('How many brazilian real do you have in your wallet now? '))
do = round(d/3.27,2)
print("Wow, you can buy ${}. Nice, isn't it?".format(do))
