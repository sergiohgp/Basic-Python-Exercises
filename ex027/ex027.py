'''
Develop a program that reads a person's name and print out the first and the last names.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        name = getName()
        Names(name)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getName():
    name = str(input('Enter your full name: ')).lower().strip()
    return name

def Names(name):
    name = name.split()
    print('Your first name is {} and your last name is {}.'.format(name[0], name[len(name)-1]))


main()