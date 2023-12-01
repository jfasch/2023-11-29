import sys
import prime

for zahl in range(1000):
    if prime.is_prime(zahl):
        print(zahl, 'ist prim')
    else:
        print(zahl, 'ist nicht prim')

