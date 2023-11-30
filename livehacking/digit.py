import sys

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

if len(sys.argv) == 1:
    digit_strs = [input('Bitte noch eine Zahl, dann hamma alles: ')]
else:
    digit_strs = sys.argv[1:]

try:
    digits = [int(ds) for ds in digit_strs]
except ValueError as e:
    print('shit happened:', e)
    sys.exit(2)

for digit in digits:
    if not 0 <= digit <= 9:
    #if digit not in range(10):
        print(digit, 'nix digit')
        sys.exit(3)

    print(translation_table[digit])
