def primes(n):
    result = []
    for number in range(n):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime:
            result.append(number)
    return result


def is_prime(m):
    if m <= 1:
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True
