# Input Format

# Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed
# by #M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
# The operation will either be S (split) or C (combine)
# M indicates method, C indicates class, and V indicates variable
# In the case of a split operation, the words will be a camel case method, class or variable name that # you need to split into a space-delimited list of words starting with a lowercase letter.
# In the case of a combine operation, the words will be a space-delimited list of words starting with
# lowercase letters that you need to combine into the appropriate camel case String.
# Methods should end #with an empty set of parentheses to differentiate them from variable names.

# Output Format

# For each input line, your program should print either the space-delimited list of words (in the case
# of a split operation) or the appropriate camel case string (in the case of a combine operation).


# Enter your code here. Read input from STDIN. Print output to STDOUT

while True:
    try:     
        sample_input = input().rstrip()
        
        # Split -> Class and Variables:
        if sample_input[0:3] == 'S;C' or sample_input[0:3] == 'S;V':   
            sample = sample_input[4:]    
            
            for i in sample:    
                if i.isupper():                    
                    index = sample.index(i)
                    if index == 0:
                        sample = i.lower() + sample[index + 1:]
                    else:              
                        sample = sample[0: index] + ' ' + i.lower() + sample[index + 1:]          
            
            print(sample)

        # Split -> Method():
        if sample_input[0:3] == 'S;M':
            sample_input = sample_input[0:-2]
            sample = sample_input[4:]    
            
            for i in sample:    
                if i.isupper():        
                    index = sample.index(i)              
                    if index == 0:
                        sample = i.lower() + sample[index + 1:]
                    else:              
                        sample = sample[0: index] + ' ' + i.lower() + sample[index + 1:]                   
            
            print(sample)

        # Combine -> Class
        if sample_input[0:3] == 'C;C':
            sample = sample_input[4:]

            for i in sample:
                if i == ' ':
                    index = sample.index(i)
                    sample = sample[0].upper() + sample[1:index] + sample[index + 1].upper() + sample[index + 2:]

            print(sample)

        # Combine -> Method()
        if sample_input[0:3] == 'C;M':
            sample = sample_input[4:]

            for i in sample:
                if i == ' ':
                    index = sample.index(i)
                    sample = sample[0:index] + sample[index + 1].upper() + sample[index + 2:]

            print(sample + '()')

        # Combine -> Variable()
        if sample_input[0:3] == 'C;V':
            sample = sample_input[4:]

            for i in sample:
                if i == ' ':
                    index = sample.index(i)
                    sample = sample[0:index] + sample[index + 1].upper() + sample[index + 2:]

            print(sample)

    except EOFError:
        break


# The best solution:
# https://programs.programmingoneonone.com/2022/05/hackerrank-camel-case-4-problem-solution.html

import re

while True:
    try:
        s = input().rstrip()    
        sc, mcv, op = s.split(";")
        if sc == "S":
            if mcv == "M":
                cap = op[:-2]                                   
                
            if mcv == "C" or mcv == "V":
                cap = op
            
            s = re.sub ("(\w)([A-Z])", r"\1 \2", cap)
            print (s.lower())
                
        if sc == "C":
            cap = op.title ()
            s = re.sub (r" ", r"", cap)
            q = s[:1].lower() + s[1:]                
            
            if mcv == "M":                                
                print (q+"()")
                
            if mcv == "C":
                print (s)
              
            if mcv == "V":
                print (q)
            
    except EOFError:
        break