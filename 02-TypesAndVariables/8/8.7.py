#Enter number: 125
#Binary number: 0b1111101
#Hexadecimal number: 0x7d

decimal = int(input('Enter int number: '))

binary = bin(decimal)
hexadecimal = hex(decimal)

print(f'Binary number: {binary}')
print(f'Hexadecimal number: {hexadecimal}')