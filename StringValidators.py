'''
Your task is to find out if the string contains: 
Alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
'''

if __name__ == '__main__':

    s = input()
    aln = 0
    alp = 0
    dig = 0
    low = 0
    upr = 0

    for i in s:
        if i.isalnum():
            aln += 1
        if i.isalpha():
            alp += 1
        if i.isdigit():
            dig += 1
        if i.islower():
            low += 1
        if i.isupper():
            upr += 1

    if aln > 0:
        print(True)
    else:
        print(False)
    if alp > 0:
        print(True)
    else:
        print(False)
    if dig > 0:
        print(True)
    else:
        print(False)
    if low > 0:
        print(True)
    else:
        print(False)
    if upr > 0:
        print(True)
    else:
        print(False)
