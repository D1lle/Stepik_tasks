a, b, new_b, code_list = input(), [], [], []
for i in range(len(a)):
    b.append(a[i])
for i in range(len(b)):
    if (b[i], b.count(b[i])) not in new_b:
        new_b.append((b[i], b.count(b[i])))
for i in new_b:
    new_b.insert(0, list(i))
    new_b.remove(i)
new_b.sort(key=lambda q: q[0])
new_b.sort(key=lambda q: q[1])
if len(new_b)==1:
    new_b[0][1] = 0
    code_list.append(new_b[0])
while len(new_b) != 1:
    code_list.append(new_b[0])
    code_list.append(new_b[1])
    letters, numbers = new_b[1][0] + new_b[0][0], new_b[1][1] + new_b[0][1]
    new_b.pop(1) and new_b.pop(0)
    position = 0
    for i in range(len(new_b)):
        if new_b[i][1] < numbers:
            position += 1
    new_b.insert(position, [letters, numbers])
    code_list[-1][1], code_list[-2][1] = 0, 1
code_list.reverse()
answer = {}
for i in b:
    code = ''
    for j in range(len(code_list)):
        if i in code_list[j][0]:
            code_list[j][1] = str(code_list[j][1])
            code += code_list[j][1]
        if j+1 == len(code_list):
            answer[i] = code
code1 = ''
for i in b:
    code1 += answer[i]
print(len(set(b)), end=' ') #unique letters
print(len(code1))
for i in answer:
    print(str(i) + ': ' + str(answer[i]))
print(code1)
