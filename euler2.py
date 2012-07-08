# generate the fibonnacci sequence up until 4 million
# Add all of the even numbers up
a = 1
b = 2
sum = 2
# while b or a is under 4 million
while (b|a) <= 4e6:
    a = a + b
    # check if number is even
    if (a / 2.0) == (round(a / 2.0)):
        sum += a
    b = a + b
    # check if number is even
    if (b / 2.0) == (round(b / 2.0)):
        sum += b
# print the sum of all the even valued fibonnacci numbers under 4million
print sum
