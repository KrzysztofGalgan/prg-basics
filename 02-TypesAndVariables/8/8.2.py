#r = 1 --> circumference = 6.28, area = 3.14
#r = 3 --> circumference = 18.84, area = 28.26
###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

pi = 3.14
radius = int(input('Enter radius: '))

area = pi * radius ** 2
circumferance = 2 * radius * pi

print(f'area = {area}')
print(f'circumferance = {circumferance}')