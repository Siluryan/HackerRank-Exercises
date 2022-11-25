#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(n, scores):
    max_count = 0
    min_count = 0
    max_ref = scores[0]
    min_ref = scores[0]
   
    for i in range(1,n):
                  
        if scores[i] > max_ref:
            max_count += 1
            max_ref = scores[i]
           
        elif scores[i] < min_ref:
            min_count += 1
            min_ref = scores[i]   

    return(list([max_count, min_count]))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))    
    
    result = breakingRecords(n, scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
