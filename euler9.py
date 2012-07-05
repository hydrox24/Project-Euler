from math import sqrt

a = 0
b = 0
c = 0

for b in range(1, 1000):
    sq_b = b**2
    for a in range(1, b+1):
        sq_a = a**2
        if b + a > 1000:
            break
        c = (1000 - b - a)
        if (c**2 == sq_b + sq_a) and (a + b + c == 1000):
            print a * b * c
            break
