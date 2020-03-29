'''
Develop a program that reads a phrase and prints
- How many times the letter A appears
- In which position is the first appearence
- In which position is the last appearence
'''

def main():
    endProgram = 'no'
    while endProgram == 'no':
        phrase = getPhrase()
        letters(phrase)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

def getPhrase():
    phrase = str(input('Enter a phrase: ')).lower().strip()
    return phrase

def letters(phrase):
    print('The phrase has {} letters \'a\''.format(phrase.count('a')))
    print('It appears at the first time in position {}.'.format(phrase.lower().find('a')+1))
    print('It appears at the last time in position {}.'.format(phrase.lower().rfind('a')+1))

main()