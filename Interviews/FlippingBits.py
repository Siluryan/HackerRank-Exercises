'''You will be given a list of 32 bit unsigned integers. 
Flip all the bits and return the result as an unsigned integer.'''

#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary_string = bin(n)[2:]
    padded_binary_string = binary_string.zfill(32)
    inverted_binary_string = ''.join('1' if bit == '0' else '0' for bit in padded_binary_string)
    result = int(inverted_binary_string, 2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
