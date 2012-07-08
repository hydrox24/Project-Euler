# What is the largest prime factor of the number 600851475143?
from math import sqrt
from sys import argv

factors = []

# lists the devisors of passed number
def divisors(n):
    for x in range(3,int(sqrt(n))+2,2):
        if n % x == 0:
            factors.append(x)

# checks if number passed is a prime
def isPrime():
    for n in factors:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        max = n**0.5 + 1
        i = 3
        
        while i <= max:
            if n % i == 0:
                return False
            i+=2

        print n

inputNum = int(argv[1])
divisors(inputNum)
print "Factors of this number are:\n"
print factors
print "\nPrime factors are:\n"
isPrime()
