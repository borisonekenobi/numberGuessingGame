import random

def canConvert(guess):
    return guess.isdigit()


def getGuess():
    guess = input(f'Guess a number between {str(guessRange[0])} and {str(guessRange[1])}: ')
    if canConvert(guess): 
        guess = int(guess)
    else: 
        print('Invalid entry!')
    return guess


def hardMode():
    for g in range(0, numGuesses):
        guess = getGuess()
        if str(type(guess)) == "<class 'str'>": continue

        if guess == num:
            print('Correct!')
            break
        else:
            print('Incorrect!')


def easyMode():
    for g in range(0, numGuesses):
        guess = getGuess()
        if str(type(guess)) == "<class 'str'>": continue

        if guess == num:
            print('Correct!')
            break
        elif guess < num:
            print('Higher!')
        else:
            print('Lower!')


def main():
    global guessRange
    global num
    global numGuesses

    guessRange = [0, 10]
    num = random.randint(guessRange[0], guessRange[1] + 1)
    numGuesses = 3

    while True:
        difficulty = input('Select a difficulty (easy, hard): ')

        if difficulty == 'easy': easyMode(); break
        elif difficulty == 'hard': hardMode(); break
        else: print('Invalid option!')


if __name__ == '__main__':
    main()