increment, found = 380, False
while not found:
    found = increment % 20 == 0 and increment % 19 == 0 and increment % 18 == 0\
    and increment % 17 == 0 and increment % 16 == 0 and increment % 15 == 0 and\
    increment % 14 == 0 and increment % 13 == 0 and increment % 12 == 0 and\
    increment % 11 == 0
    if not found:
        increment += 380
print increment
