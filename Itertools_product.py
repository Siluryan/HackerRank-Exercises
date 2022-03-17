'''
Sample Input:
1 2
3 4
Sample Output:
(1, 3) (1, 4) (2, 3) (2, 4)
'''

a = input().split()
b = input().split()
c = [(int(x), int(y)) for x in a for y in b]
d = str()

for i in c:
    d += str(i) + ' '

print(d)
