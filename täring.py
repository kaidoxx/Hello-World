import random

def dice(n):
    rolls = []
    for i in range(n):
        two_dice = random.randint(1, 6) 
        rolls.append(two_dice)
    return rolls

print(dice(5))    