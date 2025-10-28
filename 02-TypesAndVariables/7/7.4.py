#Enter tree circumference in cm: 120 
#Tree can be cut down: False

circumferance = float(input('Enter tree circumferance in cm: '))
diameter = circumferance / 3.14

print(f'Diameter = {diameter}')
print(f'Tree can be cut cown: {diameter > 50}')