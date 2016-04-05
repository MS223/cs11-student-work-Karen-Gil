range= input('Pick a range')
guess= input('Okay now pick a number in that range')
score=0
import random
random= (random.randint(1,range))
while guess != random:
    if guess < random:
        print('Guess higher')
        score= score+1
        guess= input('Guess again pick a number')
    elif guess > random:
        print('Guess lower')
        score= score+1
        guess= input('guess again pick a number')
print("YAYYYYYYYY YOU GOT IT RIGHT!!!!!!!!!")
print "It took you " + str(score) + " try to get it right"
#elif  guess == random
