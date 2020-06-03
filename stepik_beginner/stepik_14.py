'''
Substitution cipher
Need three strings:
first: letters
second: their substitutions
third: string to be encrypted
Answer is: encrypted string
'''

def make_list(string):
    a = []
    for i in string:
        a += i
    return a

String = make_list(input())
Code = make_list(input())
text = make_list(input())
cipher = make_list(input())

for i in range(len(text)):
    for j in range(len(String)):
        if text[i] == String[j]:
            text[i] = Code[j]
            break

for i in range(len(cipher)):
    for j in range(len(Code)):
        if cipher[i] == Code[j]:
            cipher[i] = String[j]
            break
for i in text:
    print(i, end='')
print()
for i in cipher:
    print(i, end='')

