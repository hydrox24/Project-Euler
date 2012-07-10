max_list = [0,0]

def length(n):
    orig = n
    list = []
    list.append(n)
    while(n != 1):
        if n % 2 == 0:
            n = n / 2
            list.append(n)
        else:
            n = 3*n + 1
            list.append(n)
    len_list = len(list)
    global max_list
    if len_list > max_list[1]:
        max_list = []
        max_list.append(orig)
        max_list.append(len_list)
    return len_list

for i in xrange(1,1000000):
    length(i)
print max_list
