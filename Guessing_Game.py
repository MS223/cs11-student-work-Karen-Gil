range= input('Pick a range')#this is going to give the computer a range of number to work with
guess= input('Okay now pick a number in that range')
score=0 #keep track of how many tries the player has used
import random
random= (random.randint(1,range))#this code take out a random number in the range. This is going to be our answer
while guess != random: #as long as the answer is incorect 
    if guess < random: #if guess the guess is lower then the answer guess lower
        print('Guess higher')
        score= score+1#tries
        guess= input('Guess again pick a number')
    elif guess > random: #if the guess is higher then the answer then guess lower
        print('Guess lower')
        score= score+1
        guess= input('guess again pick a number')
print("YAYYYYYYYY YOU GOT IT RIGHT!!!!!!!!!")
print "It took you " + str(score) + " try to get it right" # prints out the number of tries
#elif  guess == random

