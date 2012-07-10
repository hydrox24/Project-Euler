import sys
number = int(sys.argv[1])
fact = 1
for x in range(1, number+1):
    fact *= x

print fact
