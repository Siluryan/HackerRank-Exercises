# Given an array of integers, calculate the ratios of its elements that are positive,
# negative, and zero. Print the decimal value of each fraction on a new line with
# 6 places after the decimal.


#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    
    for i in arr:
        if i < 0:
            negative += 1
        elif i == 0:
            zero += 1
        else:
            positive += 1

    positive = positive / n
    negative = negative / n
    zero = zero / n

    print('%.6f\n %.6f\n %.6f' % (positive, negative, zero))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))


    plusMinus(arr)
