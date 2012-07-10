prime_list = range(1,2*(10**6)+1)
prime_list[0] = 0
maxnum = max(prime_list)

for number in prime_list:
    if number != 0:
            for instance in xrange(number*2, maxnum+1, number):
                if prime_list[instance-1]:
                    prime_list[instance-1] = 0

OldNumber = 0

for number in prime_list:
    if number != 0:
        OldNumber += number

print OldNumber
