'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

def main():
    continueProgram = 'yes'
    while continueProgram == 'yes':
        l1 = getLines()
        l2 = getLines()
        l3 = getLines()
        verifyTriangle(l1, l2, l3)
        continueProgram = input('Dou want to continue the program? ')

def getLines():
    line = float(input('Enter the measure of one line: '))
    return line

def verifyTriangle(l1, l2, l3):
    if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
        print('{}, {} and {} can\'t form a triangle.'.format(l1, l2, l3))
    else:
        print('{}, {} and {} can form a triangle.'.format(l1, l2, l3))
        if l1 == l2 and l1 == l3:
            print('And they form a triangle equilatero.')

main()