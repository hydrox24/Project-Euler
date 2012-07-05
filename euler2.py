a = 1
b = 2
sum = 2
while (b|a) <= 4e6:
    a = a + b
    if (a / 2.0) == (round(a / 2.0)):
        sum += a
    b = a + b
    if (b / 2.0) == (round(b / 2.0)):
        sum += b
print sum
