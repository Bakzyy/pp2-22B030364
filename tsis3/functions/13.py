#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
#This is how it should work when run in a terminal:

import random 

name = str(input("Hello! What is your name?\n"))

print("Well, " + name + ", I am thinking of a number between 1 and 20")

x = random.randint(1, 20)

y = 0

cnt = 0

while x != y:
    
    if cnt == 0:
        y = int(input("Take a guess.\n"))
        cnt += 1
    
    else:
        print("Your guess is too low.")
        y = int(input("Take a guess.\n"))
        cnt += 1

print("Good job, KBTU! You guessed my number in", cnt, "guesses!")