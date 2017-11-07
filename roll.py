from random import random


def roll(sides):
    sides -= 1
    return round(random() * (sides) ) + 1
    

rolled = roll(6)
print(rolled)


