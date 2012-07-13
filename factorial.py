import sys

def factorial(number):
    fact = 1
    for x in range(1, number+1):
        fact *= x
    return fact
