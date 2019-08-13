import random


def get_odd_number(a, b):
    rand = random.randrange(a, b)
    if rand % 2 == 0:
        rand += 1
    return rand


# Miller-Rabin primality test
def is_composite(n, a, r, s):
    res = pow(a, r, n)
    if res == 1 or res == n - 1:
        return False

    for _ in range(int(s)):
        res = pow(res, 2, n)
        if res == n - 1:
            return False
    return True


def is_prime(n):
    r = n - 1
    s = 0
    while r % 2 == 0:
        r //= 2
        s += 1

    limit = (n - 1) / 4
    for x in range(0, limit):
        a = random.randint(2, 100)
        if is_composite(n, a, r, s):
            return False
    return True


def generate_prime_number(a, b):
    while True:
        number = get_odd_number(a, b)
        if is_prime(number):
            return number


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Extended Euclidean algorithm
def multiplicative_inverse(e, phi):
    temp_phi = phi
    y = 0
    x = 1

    while e > 1:
        quotient = e // temp_phi
        t = temp_phi
        temp_phi = e % temp_phi
        e = t
        t = y
        y = x - (quotient * y)
        x = t

    if x < 0:
        x += phi

    return x
