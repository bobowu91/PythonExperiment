import math
from pytimer import process_time
import numpy as np


@process_time
def prime_n(n):
    '''
    Parameters
    ----------
    n : integer
    how many prime number you would like to generate.

    Returns
    -------
    prime : list
    Return a list of prime numbers.
    '''
    prime = [2]
    i = 3

    while len(prime) < n:
        for p in prime:
            if i % p == 0:
                break
        if i % p != 0:  # this means we didn't reach here by break the loop
            prime.append(i)
        i = i + 1
    return prime


@process_time
def prime_n_fast(n):
    prime = [2]
    num = 3
    while len(prime) < n:
        # filtering out all even numbers
        if num % 2 == 0:
            num = num + 1
            continue
        # from the first prime number in list to square root of the number
        for i in range(prime[0], int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:  # for-else check if ALL previous prime is divisible
            prime.append(num)
        num = num + 1
    return prime


@process_time
def prime_below_n(n):
    prime = [2]
    i = 3
    while prime[-1] < n:
        for p in prime:
            if i % p == 0:
                break
        if i % p != 0:  # this means we didn't reach here by break the loop
            prime.append(i)
        i = i + 1
    return prime


@process_time
def factorised_n_by_prime(n, prime):

    # prime = prime_below_n(n)
    fac = []
    factors = []

    if n in prime:
        return n

    for p in prime:
        if n % p == 0:
            fac.append(p)

    for f in fac:
        while n % f == 0:
            factors.append(f)
            n = n/f
    return factors


@process_time
def factors(n):
    prime = [2]
    i = 2
    n_factor = []

    while True:
        # part 1: check for one prime factor
        factor = prime[-1]
        # print(f"for facor: {factor}")
        while n % factor == 0:
            n = n / factor
            # print(f"now the reminder is {n}")
            n_factor.append(factor)
            # print(f"now the prime factor includes: {n_factor}")
        if n == 1:  # n here is the reminder from the previous prime number
            # print(f"now factor {factor} is done.")
            break  # if the whole number is fully divided; break the loop
        # print("----------------------------------")

        # part 2: generate the next prime number
        while True:
            i = i + 1
            for p in prime:
                if i % p == 0:  # check all previous prime numbers
                    break  # if any previous prime is divisible; then abandon i
            if i % p != 0:
                prime.append(i)
                break

    return n_factor


@process_time
def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2,)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i,)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


# m = prime_n(30000)
# print(m[-1])
# primeFactors()
# prime_n(n)
n = 100000
# x = prime_n_fast(n)
# print(x[-1])

primeFactors(1299709)


'''
Results: 7,489,327,492
runtime of factors : 0.004639668999999999
[2, 2, 17, 17, 2221, 2917]

Results: 8,050,487
runtime of factors : 14.152265192
[29, 277603]

Results: 84,902,834,903,284
runtime of factors: 14.567951247
[2, 2, 113, 293, 2179, 294211]

# too long
Results: 3,489,232,754,192
Results: 66,657,389,475
'''

# prime_num = prime_below_n(4327)
# result = factorised_n_by_prime(16817, prime_below_n(16817))
# print(result)


'''
# n_prime = 10
# prime = [2]
# print(prime)
#
# for i in range(3, 500):
#     for p in prime:
#         if i % p == 0:
#             break
#     if i % p != 0:  # this means we didn't reach here by break the loop
#         prime.append(i)
# print(prime)

def kk(n):

    while True:
        print(f"P1 n is equal to {n}")
        if n - 1 < 10:
            print(f"P2 n is equal to {n}")
            break
        print(f"P3 n is equal to {n}")
        n = n - 2
        print(f"P4 n is equal to {n}")
        print("***********************")

    return n


f = kk(15)
print(f)

lis = list(np.arange(3, 20))
print(lis)
number = 39

for i in range(lis[0], int(math.sqrt(number))):
    print(i)
print(math.sqrt(number))

lis = [1, 3, 23, 4, 5]
for i in lis:
    if i % 2 == 0:
        print(f'{i} is an even number')
        break
else:
    print('in this case, for-else will happen')
'''
