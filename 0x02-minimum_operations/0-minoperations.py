#!/usr/bin/python3
""" Minimum Operations Module """


def minOperations(n):
    """ Returns the number of minimum operations required """
    if n <= 1:
        return 0

    counter = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            counter += divisor
            n //= divisor
        else:
            divisor += 1

    return counter