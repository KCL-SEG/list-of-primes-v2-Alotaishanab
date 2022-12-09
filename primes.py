"""List of prime numbers generator."""
from math import sqrt

"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError
    list_of_primes = [2]
    counter = 3
    while len(list_of_primes) < number_of_primes:

        for i in list_of_primes:
            if counter % i == 0:
                break
            if i >= sqrt(counter + 1):
                list_of_primes.append(counter)
                break
        counter += 1
    return list_of_primes

