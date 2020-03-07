#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
v = float(input('Write a measure in meters: '))
vcm = v*10**2
vmm = v*10**3
print('Your measure is {}m, {}cm and {}mm.'.format(v,vcm,vmm))
