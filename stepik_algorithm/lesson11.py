def BinSearch(l, r, enter, enter2):
    while l <= r:
        m = (l + r)//2
        if enter2[i] == enter[m]:
            return m+1
        if l == r - 1:
            return -1
        elif enter2[i] > enter[m]:
            l = m
            continue
        else:
            r = m
            continue
# Binary search algorithm
enter = [int(i) for i in input().split()]
enter2 = [int(i) for i in input().split()]
# Result - indexes of integers from enter2 in enter

l = 0
r = len(enter)
for i in range(len(enter2)):
    print(BinSearch(l, r, enter, enter2), end=' ')


