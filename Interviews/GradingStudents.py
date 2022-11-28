'''Sam is a professor at the university and likes to round
each student's grade according to these rules:
- If the difference between the grade and the next multiple of 5
is less than 3, round grade up to the next multiple of 5.
- If the value of grade is less than 38, no rounding occurs
as the result will still be a failing grade.'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    gd = grades    
    rd = int()

    for i in range(len(gd)):
        rd = (gd[i]//5)*5 + 5
        if rd - gd[i] < 3 and gd[i] >= 38:
            gd[i] = rd

    return(gd)
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
