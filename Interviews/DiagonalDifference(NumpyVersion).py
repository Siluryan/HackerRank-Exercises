#!/bin/python3
import numpy as np

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    arr = np.array(arr)
    main_diagonal = np.trace(arr)
    secondary_diagonal = np.trace(np.fliplr(arr))

    return abs(int(main_diagonal) - int(secondary_diagonal))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)

    print(result)