'''
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
'''

def count_substring(string, sub_string):
    count = 0
    frs_i = 0
    lst_i = len(sub_string)
       
    for i in string:
        if sub_string == string[frs_i:lst_i]:
            count += 1
        
        frs_i += 1
        lst_i += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
