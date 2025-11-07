###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))
quarter = 0

if month >= 10 and month <= 12:
    quarter = 4
elif month < 10 and month > 6:
    quarter = 3
elif month <= 6 and month > 3:
        quarter = 2
elif month < 4 and month >= 1:
    quarter = 1
else:
     print('Wrong input')
print(f'Month {month} is in quarter {quarter}')