#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Write a number: '))
d = n*2
t = n*3
sr = n**(1/2)
print("You choose {}. It's double is {}, triple is {} and square root is {}.".format(n,d,t,sr))
