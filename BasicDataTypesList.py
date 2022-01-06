'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer (e) at position (i)
print: Print the list.
remove e: Delete the first occurrence of integer (e)
append e: Insert integer (e) at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of followed by lines of commands where each command will be of the types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__ == '__main__':
    N = int(input())
    A = []

    for i in range(N):
        c, *p = input().split()
        p = [int(v) for v in p]
        if len(p) == 0:
            pass
        elif len(p) == 1:
            e = p[0]
        elif len(p) == 2:
            i = p[0]
            e = p[1]

        if c == 'insert':
            A.insert(i, e)
        elif c == 'print':
            print(A)
        elif c == 'remove':
            A.remove(e)
        elif c == 'append':
            A.append(e)
        elif c == 'sort':
            A.sort()
        elif c == 'pop':
            A.pop()
        elif c == 'reverse':
            A.reverse()
