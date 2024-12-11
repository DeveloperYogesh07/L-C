# program is to Roll the Dice
import random

def roll_dice(sides):
    """Simulates rolling a dice with the given number of sides."""
    result = random.randint(1, sides)
    return result

def main():
    """Main function to simulate a dice rolling game."""
    dice_sides = 6
    continue_rolling = True

    while continue_rolling:
        user_input = input("Ready to roll the dice? Enter Q to quit: ")
        if user_input.lower() != "q":
            dice_result = roll_dice(dice_sides)
            print("You have rolled a", dice_result)
        else:
            continue_rolling = False
