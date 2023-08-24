
x = int(input())
y = int(input())
mat = []
for i in range(x):
    arr = input().split()
    mat.append(arr)
k=str()

k = input("Enter the word :")
l = len(k)

r = []
for i in k:
    r.append(i)
rev = r[-1]

for i in range(2, len(r)+1):
    rev += r[-1*i]

for i in range(x):
    t = str()
    for j in range(y-l+1):
        for n in range(j, j+l):
            if n == j:
                t = mat[i][n]
            else:
                t += mat[i][n]
        if t == k:
            print("We found the word initially at", i+1, "Row", j+1, "Column in a horizontal way")
            exit(0)
        if t == rev:
            print(rev)
            print("We found the word initially at", i+1, "Row", j+1, "Column in a reversed horizontal way")
            exit(0)


for i in range(y):
    t = str()
    for j in range(x-l+1):
        for n in range(j, j+l):
            if n == j:
                t = mat[n][i]
            else:
                t += mat[n][i]
            if t == k:
                print("We found the word initially at", j+1, "Row", i+1, "Column in a vertical way")
                exit(0)
            if t == rev:
                print(rev)
                print("We found the word initially at", j + 1, "Row", i + 1, "Column in a reversed vertical way")
                exit(0)


for i in range(x):
    t = str()
    for j in range(y):
        a = i
        b = j
        for n in range(l):
            if a == i:
                t = mat[a][b]
            else:
                t += mat[a][b]
            if t == k:
                print("We found the word initially at", i + 1, "Row", j + 1, "Column in a diagonal way")
                exit(0)
            if t == rev:
                print(rev)
                print("We found the word initially at", i + 1, "Row", j + 1, "Column in a reversed diagonal way")
                exit(0)
            if a == x-1 or b == y-1:
                break
            a += 1
            b += 1
print("No such word found")
