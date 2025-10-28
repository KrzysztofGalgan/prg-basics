###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code - 1
if (number_of_letters == 1):
    print(f'Between {first} and {last} is 1 letter')
if (number_of_letters > 1):
    print(f'Between {first} and {last} are {number_of_letters} letters')