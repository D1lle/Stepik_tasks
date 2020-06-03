a, n = map(lambda i: int(i), input().split())
codename = {}
for i in range(a):
    z = input().split(': ')
    codename[z[0]] = z[1]
b = input()
code = []
for i in range(len(b)):
    code.append(b[i])
answer = []
temp = ''
for j in range(n):
    temp += code[0]
    code.pop(0)
    for i in codename:
        if temp == codename[i]:
            answer.append(i)
            temp = ''
            continue
for i in answer:
    print(i, end='')

