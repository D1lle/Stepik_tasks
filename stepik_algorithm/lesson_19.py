def EditDistBU(A, B):
    n = len(A)
    m = len(B)
    D = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        D[0][i] = i
    for j in range(m):
        D[j][0] = j
    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]:
                c = 0
            else:
                c = 1
            D[j][i] = min(
                [D[j - 1][i] + 1, D[j][i - 1] + 1, D[j - 1][i - 1] + c])
    return D[m-1][n-1]
# Levenshtein distance of 2 strings

A, B = [], []
a = input()
b = input()
for i in a:
    A += i
for j in b:
    B += j
A.insert(0, ' ')
B.insert(0, ' ')
print(EditDistBU(A, B))
