'''
Develop a program that reads the name of a city and prints if begins or not with 'SANTO'.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        inputData()
        endProgram = input('Do you want to end the program?(Enter yes or no): ')

def inputData():
    city = input('Enter the city\'s name: ')
    c = city.split()
    if c[0].lower() == 'santo':
        print('Your city begins with santo!')
    else:
        print('Your city doesn\'t begin with santo.')

main()