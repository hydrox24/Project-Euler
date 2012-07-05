square_of_sums = 0
sum_of_squares = 0

for i in range(1,101):
    square_of_sums += i

print square_of_sums**2

for i in range(1,101):
    sum_of_squares += i**2

print sum_of_squares

print (sum_of_squares - square_of_sums**2 )
