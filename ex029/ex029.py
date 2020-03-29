'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        speed = getSpeed()
        calcSpeed(speed)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getSpeed():
    speed = int(input('Enter the speed of the vehicle (only integer values): '))
    return speed

def calcSpeed(speed):
    if speed > 80:
        print('You exceeded the speed limit. You will receive a ticket of ${}.'.format(calcTicket(speed)))
    else:
        print('You did not exceed the speed limit.')

def calcTicket(speed):
    ticket = (speed - 80)*7
    return ticket

main()