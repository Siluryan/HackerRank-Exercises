'''
In this challenge, you will be given 2 integers, n and m. 
There are n words, which might repeat, in word group A. There are m words belonging to word group B. 
For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. 
If it does not appear, print -1. '''

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
    
for i in range(m):
    print (' '.join(d[input()]) or -1)

  
# No defaultdict() version:

n_size, m_size = map(int,input().split()))
a = list()
b = list()
result = list()
x = 0
y = 1
c = 0

for i in range(n_size):
	n = input()
	a.append(n)

for i in range(m_size):
	m = input()
	b.append(m)

for i in range(len(b)):
	for i in b[x:y]:
		if i not in a:
			print('-1')
		else:
			for n in a:
				if n == i:
					result.append(c+1)

				c += 1
			result = str(result).replace(',','')
			result = result.strip('[]')
			print(result)
			x += 1
			y += 1
			c = 0
			result = list()
