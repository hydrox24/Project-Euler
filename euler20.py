from factorial import factorial

fact = factorial(100)
fact_list = list(str(fact))

x = 0
for digit in fact_list:
    x += int(digit)

print x
