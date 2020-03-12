# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input('How many days you used the car? '))
k = float(input('How many kilometers do you run? '))
s = round(60*d+0.15*k,2)
do = round(s*4.2,2)
print('So, you used the car for {} days and run {}km. The total cost is R${} and ${}. Thanks for the preference.'.format(d,k,s,do))
