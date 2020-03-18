'''
Develop a program that reads a number between 0 and 9999 and show each one split
'''

'''def integer():
    num = int(input('Enter a integer number between 0 and 9999: '))
    while num < 0 and num > 9999:
        print('Number out of range, please try again.')
        num = int(input('Enter a integer number between 0 and 9999: '))
    else:
        if num > 0 and num <= 9:
            print('unidade: '+num)
        elif num > 9 and num <= 99:

            print('unidade')
        elif num > 99 and num <= 999:
        else:
#integer()
'''

def strg():
    num = input('Enter an integer number between 0 and 9999: ')

    while len(num) > 4:
        print('Number out of range. Try again.')
        num = input('Enter an integer number between 0 and 9999: ')
    else:
        if len(num) == 1:
            print("""
unidade: {} 
dezena: 0
centena: 0
milhar: 0""".format(num))
        elif len(num) == 2:
            print("""
unidade: {}
dezena: {}
centena: 0
milhar: 0""".format(num[1],num[0]))
        elif len(num) == 3:
            print("""
unidade: {} 
dezena: {}
centena: {}
milhar: 0""".format(num[2],num[1],num[0]))
        else:
            print("""
unidade: {} 
dezena: {}
centena: {}
milhar: {}""".format(num[3], num[2], num[1], num[0]))

strg()