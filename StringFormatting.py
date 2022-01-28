'''
Given an integer, n, print the following values for each integer i from 1 to n :
-> Decimal
-> Octal
-> Hexadecimal (capitalized)
-> Binary
'''

def print_formatted(n):
    # your code goes here
    for i in range(n):
        i += 1
        dc = str(i).rjust(len(bin(n))-2)
        ict = oct(i)
        ict = ict.lstrip('0o')
        ct = str(ict).rjust(len(bin(n))-2)
        ihx = hex(i)
        ihx = ihx.lstrip('0x')
        hx = str(ihx).rjust(len(bin(n))-2)
        ibn = bin(i)
        ibn = ibn.lstrip('0b')
        bn = str(ibn).rjust(len(bin(n))-2)
        
        print(f'{dc} {ct} {hx.upper()} {bn}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
