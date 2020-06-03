def InsertSiftUp(list, x):
    list.append(x)
    a = len(list)
    i = list.index(x, a-1)
    while list[i] > list[(i-1)//2] and i != 0:
        list[i], list[(i-1)//2] = list[(i-1)//2], list[i]
        i = (i-1)//2

def ExtractMaxSiftDown(list):
    if len(list) == 1:
        ans = list.pop(0)
        return ans
    save = list.pop(-1)
    list.insert(0, save)
    save = list.pop(1)
    a = len(list)
    i = 0
    while 2 * i + 1 < a:
        left = 2 * i + 1
        right = 2 * i + 2
        j = left
        if right < a and list[right] > list[left]:
            j = right
        if list[i] > list[j]:
            break
        list[i], list[j] = list[j], list[i]
        i = j
    return save

n, heap = int(input()), []
# Insert x, where x - integer
# or ExtractMax
# Creates the priority queue
for i in range(n):
    command = input().split()
    if command[0] == 'Insert':
        InsertSiftUp(heap, int(command[1]))
    elif command[0] == 'ExtractMax':
        print(ExtractMaxSiftDown(heap))