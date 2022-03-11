'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

Best solution i found:
s = input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"
    
https://www.hackerrank.com/abitrolly
'''

def minion_game(string):
    # your code goes here
    substring = str()
    liststring = list()
    vowels = ['A','E','I','O','U']
    listvowels = list()
    listconsonants = list()
    vct = 0
    cct = 0
    ct1 = 0
    ct2 = 1

    while ct2 <= len(string):
        substring = string[ct1:ct2]
        liststring.append(substring)
        ct2 +=1
        if ct2 > len(string):
            ct1 += 1
            ct2 = ct1+1

    for i in liststring:
        if i[0] in vowels:
            listvowels.append(i)
        else:
            listconsonants.append(i)

    for i in listvowels:
        vct += 1
    for i in listconsonants:
        cct += 1

    if vct > cct:
        print(f'Kevin {vct}') 
    elif cct > vct:
        print(f'Stuart {cct}')
    else:
        print('Draw')  


if __name__ == '__main__':
    s = input()
    minion_game(s)
