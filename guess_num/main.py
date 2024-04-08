# gues the number game

import random

while True:
    chances = 3
    num = random.randint(1, 10)
    is_true = False

    while chances > 0:
        guess = int(input("Guess a number between 1 to 10: "))

        if guess < num:
            print("Your guess is too low")
            chances -= 1
        elif guess > num:
            print("Your guess is too high")
            chances -= 1
        elif guess == num:
            print("Your guess is right")
            is_true = True
            break
    
    if chances == 0:
        print("Game over")
        print("The number was", num)
        print("Would you like to play again? (Y/N)")
        choice = input()
        if choice == "Y" or choice == "y":
            continue
        else:
            print("Thank you for playing")
            break
    elif is_true:
        print("Would you like to play again? (Y/N)")
        choice = input()
        if choice == "Y" or choice == "y":
            continue
        else:
            break
