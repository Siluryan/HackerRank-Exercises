'''Given an array of integers, where all elements but one occur twice,
find the unique element.'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    dic = dict()
    count = int()
    for i in a:
        dic[i] = dic.get(i, 0) + 1
        
    for k, v in dic.items():
        if v == 1:
             return(k)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
