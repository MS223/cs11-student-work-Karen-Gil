range= input('Pick a range')
guess= input('Okay now pick a number in that range')

import random
random= (random.randint(1,range))
while guess != random:
    if guess < random:
        print('Guess higher')
        guess= input('Guess again pick a number')
    elif guess > random:
        print('Guess lower')
        guess= input('guess again pick a number')
#elif  guess == random
print("YAYYYYYYYY YOU GOT IT RIGHT!!!!!!!!!")
