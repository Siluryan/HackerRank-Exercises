# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s, p):      
    
    if s[-2:] == 'PM' and p == 12:        
        return(s[0:8])
    elif s[-2:] == 'PM':
        p = p + 12
        return(str(p) + s[2:8])
    elif s[-2:] == 'AM' and p == 12:
        return('00' + s[2:8])
    else:
        return(s[0:8]) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    pm_hour = s[0:2]
    pm_hour = int(pm_hour)

    result = timeConversion(s, pm_hour)

    fptr.write(str(result) + '\n')

    fptr.close()
