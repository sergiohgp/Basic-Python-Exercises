#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
h = float(input("What is the wall's height in meters? "))
wd = float(input("What is the wall's width in meters? "))
a = round(h*wd,2)
t = round(a/2,2)
print("Well, your wall is {}m height and {}m width. It's area is {}m^2. You'll need {}l of tint to paint the whole wall.".format(h,wd,a,t))

