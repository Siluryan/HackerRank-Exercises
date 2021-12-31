'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

if __name__ == '__main__':
    n = int(input())
    s_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        s_marks[name] = scores
    query = input()
    
    marks = s_marks[query]
    avg = sum(marks)/len(marks)
    
    print(f'{avg:.2f}')
