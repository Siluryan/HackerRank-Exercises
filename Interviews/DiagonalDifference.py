#!/bin/python3
import os
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    tamanho = len(arr)
    
    main_diagonal = sum(arr[i][i] for i in range(tamanho))
    secondary_diagonal = sum(arr[i][tamanho - i - 1] for i in range(tamanho))    
    
    return abs(main_diagonal - secondary_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
