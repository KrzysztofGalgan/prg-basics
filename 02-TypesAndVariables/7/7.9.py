#Dice rolled: 4
#Special number (1 or 6): False

import random

dice = random.randint(1,6)

print(f'Dice rolled: {dice}')
print(f'Special number (1 or 6): {dice == 1 or dice == 6}')