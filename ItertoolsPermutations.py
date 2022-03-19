'''
Sample Input:
HACK 2

Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
from itertools import permutations

s, k = input().split()
s = sorted(list(s))
k = int(k)

pm = list(permutations(s,k))

for i in pm:
    new_i = ''.join(i)
    print(new_i)
