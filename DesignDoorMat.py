'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
    
    Mat size must be N x M (N is an odd natural number, and M is 3 times N)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Design:

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

Output the design pattern.  
'''
    
if __name__ == '__main__':

	N, M = input().split()
	N = int(N)
	M = int(M)
	W = 'WELCOME'
	p = '.|.'
	d = 1
	i = 0	
	
	while i < int((N-1)/2): 
		print((p*d).center(M,'-'))
		i += 1
		d += 2
		
	print(W.center(M,'-'))
	i = 0
	d = N-2
	
	while i < int((N-1)/2): 
		print((p*d).center(M,'-'))
		i += 1
		d -= 2
