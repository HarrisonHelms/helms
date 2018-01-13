from random import random
import math
import time

#sides = 6


def roll(sides):
    R = random()      # [0,1)
    rolled = (sides * R)
    rolled += 1
    rolled = math.floor(rolled)
    return rolled

k = roll(6)
print(k)

