'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
'''

def main():
    print('Welcome to the program!')
    print()
    endProgram = 'no'
    while endProgram == 'no':
        name = getName()
        silvaInName(name)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getName():
    name = input('Enter your full name: ')
    return name

def silvaInName(name):
    name = name.split()
    for i in range(0,len(name)):
        if name[i].lower() == 'silva':
            print('You have Silva in your name. Your {}º name is Silva.'.format(i+1))





main()