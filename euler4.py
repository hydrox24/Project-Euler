numberlist = []
for x in range(100, 999):
    for y in range(100, 999):
        numberlist.append(x * y)

palindromes = []

for i in numberlist:
    if (i % 11) == 0:
        string = "%s" % i
        if string == string[::-1]:
            palindromes.append(i)

palindromes.sort()
print palindromes
