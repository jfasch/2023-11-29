import sys

number = 53

if number == 1:
    print('not prime')
    sys.exit()

divisor_candidate = 2

while divisor_candidate < number:
    if number % divisor_candidate == 0:
        print('not prime, divisor:', divisor_candidate)
        break
    else:
        divisor_candidate += 1
else:
    print('prime')
