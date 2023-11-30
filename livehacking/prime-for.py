import sys

number = int(sys.argv[1])

if number == 1:
    print('not prime')
    sys.exit()

for divisor_candidate in range(2, number):
    if number % divisor_candidate == 0:
        print('not prime, divisor:', divisor_candidate)
        break
else:
    print('prime')
