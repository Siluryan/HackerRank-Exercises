'''
You are given an integer,(n). 
Your task is to print an alphabet rangoli of size(n).
Rangoli is a form of Indian folk art based on creation of patterns.

E.g.(n = 5)

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

import string


def print_rangoli(size):
    size -= 1
    #center line:
    s = string.ascii_lowercase[1:size+1]
    rs = string.ascii_lowercase[size::-1]
    cl = '-'.join(rs+s)
    
    #alignment:
    ls = len(cl)
    
    #upside:
    for i in range(size):
        rs = string.ascii_lowercase[size:size-i:-1]
        s = string.ascii_lowercase[size-i:size]
        lt = string.ascii_lowercase[size]
        sd = '-'.join(rs+s+lt)
        i += 1
        print(sd.center(ls,'-'))

    print(cl)
    
    #bottom:
    for i in range(size):
        rs = string.ascii_lowercase[size:i+1:-1]
        s = string.ascii_lowercase[i+1:size]
        lt = string.ascii_lowercase[size]
        sd = '-'.join(rs+s+lt)
        i += 1
        print(sd.center(ls,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
