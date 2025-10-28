###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
print('"." is a decimal separator')

temperatura_celsjusz = float(input('Enter temperature(C): ')) #Pobranie temperatury z konsoli

temperatura_kelvin = temperatura_celsjusz + 373.1 #Konwersja na celviny

temperatura_fahrenheit = temperatura_celsjusz * 1.8 + 32 #Konwersja na fahrenheity

print(f'Kelvin: {temperatura_kelvin}') #Wypisanie wyniku
print(f'Fahrenheit: {temperatura_fahrenheit}')