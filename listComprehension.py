''' Let's learn about list comprehensions!
You are given three integers (x, y, z) and representing the dimensions of a cuboid along with an integer (n).
Print a list of all possible coordinates given by (y, j, k) on a 3D grid where the sum of i + j + k is not equal to (n). 
Please use list comprehensions rather than multiple loops, as a learning exercise. '''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = 0
    ia = [i]
    j = 0
    ja = [j]
    k = 0
    ka = [k]
    results = []

while i < x:
    i += 1
    ia.append(i)

while j < y:
    j += 1
    ja.append(j)

while k < z:
    k += 1
    ka.append(k)

for i in ia:
    for j in ja:
        for k in ka:
            if i + j + k != n:
                results.append([i, j, k])

print(results)
