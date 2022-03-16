'''
Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output

AB
CA
AD
'''
def merge_the_tools(string, k):
    c = 0
    l = list()
    
    while c < len(string):
        substring = string[c:c+k]
        l.append(''.join(dict.fromkeys(substring)))
        c += k
    
    for i in l:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
