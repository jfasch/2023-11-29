import sys
import prime

number = int(sys.argv[1])

if prime.is_prime(number):
    print('prime')
else:
    print('not prime')
    

