def is_prime(number):
    if number < 2:
        return False
    for x in range(2, n):
        if number % x == 0:
            return False
    return True