'''
Given the names and grades for each student in a class of students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''

if __name__ == '__main__':

    N = []
    slist = []

    for i in range(int(input())):
        name = str(input())
        score = float(input())
        slist.append(score)
        N.append([name, score])

    slist = sorted(set(slist))
    sec_low = slist[1]
    
    nlist = [name for name, score in N if score == sec_low]
    nlist = sorted(nlist)
    
    for name in nlist:
        print(name)
