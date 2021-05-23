import random


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        roll_of_dice = (x, y)
        return roll_of_dice

dice = Dice()
# dice.roll()
print(dice.roll())
