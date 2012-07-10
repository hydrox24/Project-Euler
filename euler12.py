from math import sqrt
#creates a triangle number
def triangulate(n):
    x = 0
    for i in xrange(1,n+1):
        x += i
    return x

#lists the devisors of passed number
def divisors(n):
    factors = []
    for x in range(1,int(sqrt(n))+1):
        if n % x == 0:
            factors.append(x)
            factors.append(n/x)
    return factors

i = 0
while(True):
    triangle = triangulate(i)
    if len(divisors(triangle)) > 500:
        print triangle
        break
    i +=1
