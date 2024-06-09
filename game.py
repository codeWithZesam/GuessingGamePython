# Guessing game
import math 
import random
# User input for lowest and highest guess
lower = int(input("Enter Lower Bound:-"))
upper = int(input("Enter Upper Bound:-"))

# Random number chooses by system
x = random.randint(lower,upper)
print("\n\t\tYou've only " + str(round(math.log(upper - lower + 1,2))) + " chances to guess integer.\n")
count = 0

while count < math.log(upper - lower + 1,2):

    guess = int(input("Guess any number?"))
    count += 1

    if guess == x:
        print("\n\t\tCongratulation! You Did It In " + str(count) + " Try.")

        break
    elif guess > x:
        print("Number is too high.")
    else:
        print("Number is too low")
#if limited guesses are crossed
if count >= math.log(upper - lower + 1,2):
    print("\n\nYour Guess Are Wrong.")
    print("Better Luck Next Time!!")
