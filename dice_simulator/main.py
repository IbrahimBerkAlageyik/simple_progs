
import random


class Dice:

    def __init__(self, side):
        self.side = side

    def roll(self):
        return random.randint(1, self.side)

dice_list = []
def create_multiple_dice(num):
    side = int(input("Enter the number of sides: "))
    for i in range(num):
        dice = Dice(side)
        dice_list.append(dice)
    print("Dices created successfully")

        

def create_single_dice():
    side = int(input("Enter the number of sides: "))
    dice = Dice(side)
    dice_list.append(dice)
    print("Dice created successfully")

def roll_all_dices():
    print("Rolling all dices...")
    for dice in dice_list:
        print("Rolling the dice...")
        print(f"Result: \t {dice.roll()}")

def roll_single_dice(dice):
    print("Rolling the dice...")
    print(dice.roll())

def see_all_dices():
    index = 0
    print("Index \t Side")
    for dice in dice_list:
        print(f"{index} \t {dice.side}")
        index += 1

while True:
    print("1. Create multiple dices")
    print("2. Create single dice")
    print("3. Roll all dices")
    print("4. Roll single dice")
    print("5. See all dices")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter the number of dices you want to create: "))
        if num <= 0:
            print("Invalid number of dices")
            continue
        else:
            create_multiple_dice(num)
    elif choice == 2:
        create_single_dice()
    elif choice == 3:
        roll_all_dices()
    elif choice == 4:
        dice_index = int(input("Enter the index of the dice you want to roll: "))
        if dice_index < 0 or dice_index >= len(dice_list):
            print("Invalid index")
            continue
        else:    
            roll_single_dice(dice_list[dice_index])
    elif choice == 5:
        see_all_dices()
    elif choice == 6:
        break
    else:
        print("Invalid choice")








