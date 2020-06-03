n = int(input())
segments = []
for i in range(n):
    segments += [list(map(lambda x: int(x), input().split()))]
dots_coordinates = []
segments.sort(key=lambda q: q[1])
current_dot = segments[0][1]
dots_coordinates += [segments[0][1]]
dots = 1
for i in range(len(segments)):
    if segments[i][0] <= current_dot <= segments[i][1]:
        continue
    else:
        dots_coordinates += [segments[i][1]]
        current_dot = segments[i][1]
        dots += 1

print(dots)
print(*dots_coordinates)

