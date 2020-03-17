'''
O mesmo professor do problema anterior quer sortear a ordem de apresentacao dos mesmos alunos.
Faca um programa que sorteie a ordem de apresentacao e a mostre.
'''
import random
def main():
    a1 = str(input("Student one's name: "))
    a2 = str(input("Student two's name: "))
    a3 = str(input("Student three's name: "))
    a4 = str(input("Student four's name: "))
    y = [a1, a2, a3, a4]
    x = random.sample(y,4)
    print('The order of the presentation is: {}.'.format(x))

main()