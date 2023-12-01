def is_prime(n):
    if n == 1:
        return False
    
    for divisor_candidate in range(2, n):
        if n % divisor_candidate == 0:
            return False

    return True
