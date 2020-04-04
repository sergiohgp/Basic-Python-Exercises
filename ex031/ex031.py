'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        n = getDistance()
        calcFare(n)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getDistance():
    distance = float(input('Enter the distance of the trip: '))
    return distance

def calcFare(distance):
    if distance <= 200:
        fare = distance*.50
        print('For this trip, your fare is ${}.'.format(fare))
    else:
        fare = distance*.45
        print('For this trip, your fare is ${}.'.format(fare))


main()