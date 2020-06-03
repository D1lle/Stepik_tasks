'''
Starting in coordinates 0;0
Need to input number of steps
Then these steps
Example:
2
North 20
West 35

Result is finish coordinates
'''

Num_of_steps = int(input())
step = []
step1 = []
for i in range(Num_of_steps):
    step = input().split()  #step
    step1.append(step)      #all steps
for i in range(Num_of_steps):
    step1[i][1] = int(step1[i][1])
coordinates = [0, 0]
for i in range(Num_of_steps):
    if step1[i][0] == 'east':
        coordinates[0] += step1[i][1]
    elif step1[i][0] == 'west':
        coordinates[0] -= step1[i][1]
    elif step1[i][0] == 'north':
        coordinates[1] += step1[i][1]
    elif step1[i][0] == 'south':
        coordinates[1] -= step1[i][1]
print(*coordinates)