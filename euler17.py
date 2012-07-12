import re
words_ones = {\
        1: 'one',\
        2: 'two',\
        3: 'three',\
        4: 'four',\
        5: 'five',\
        6: 'six',\
        7: 'seven',\
        8: 'eight',\
        9: 'nine',\
        11: 'eleven',\
        12: 'twelve',\
        13: 'thirteen'}

words_tens = {\
        1: 'ten',\
        2: 'twenty',\
        3: 'thirty',\
        4: 'fourty',\
        5: 'fifty',\
        6: 'sixty',\
        7: 'seventy',\
        8: 'eighty',\
        9: 'ninety'}

for num in range(1,1000+1):
    num_list = " ".join(str(num)).split(" ")
    try:
        print words_ones[int(num_list[-1])]
    except KeyError:
        if num_list[-1] == 1 or num_list[-1] == 2 num_list[-1] == 3
            print words_ones[10]
        elif num_
        #print words_ones[int(num_list[-2]+"0")]
