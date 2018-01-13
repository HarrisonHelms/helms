from random import random

R = random()
sides = input("Enter the number of sides on the die: ")

'''
rolled = (sides - 1) * R
rolled = round(rolled)
rolled += 1
'''

def roll(sides):
    rolled = (sides - 1) * R
    rolled = round(rolled)
    rolled += 1
    return rolled

num = roll(int(sides))
num = str(num)
print("Your random roll is: " + num)

