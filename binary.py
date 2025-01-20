binary = input("Enter a binary number: ")
decimal = 0
fraction = 0.0

if '.' in binary:
    integer, fract = binary.split('.')
else:
    integer = binary
    fract = ''

for i in range(len(integer)):
    digit = int(integer[i])
    power = len(integer) - i - 1
    decimal += digit * 2 ** power


for i in range(len(fract)):
    digit = int(fract[i])
    power = i + 1
    fraction += digit * 2 ** -power

decimal += fraction
print(f"Decimal equivalent: {decimal}")