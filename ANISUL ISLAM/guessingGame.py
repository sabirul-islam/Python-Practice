from random import randint

for i in range(1, 6):
    guessNumber = int(input('Enter Number Between 1 to 5 : '))

    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print('You Won The Game')

    else:
        print('You Lost, Try Again.')
        print('random Number Was : ', randomNumber)