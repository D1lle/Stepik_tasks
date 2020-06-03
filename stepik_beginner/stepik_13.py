'''
Input - number of games and their results
Result - stat table

Example input:
4
Tottenham;2;Arsenal;5
MU;0;MC;3
Arsenal;3;MC;1
Tottenham;2;MU;2

Result:
Tottenham:2 0 1 1 1
Arsenal:2 2 0 0 6
MU:2 0 1 1 1
MC:2 1 0 1 3
(team):(matches) (won) (draw) (lost) (points)
'''


def team_stat(team, result):
    a = [0, 0, 0, 0, 0]

    
    if result == 'win':
        a[0] += 1
        a[1] += 1
        a[4] += 3
    elif result == 'lost':
        a[0] += 1
        a[3] += 1
    elif result == 'draw':
        a[0] += 1
        a[2] += 1
        a[4] += 1

    return a
total_table = {}
total_stats = [0, 0, 0, 0, 0]
teams = set()
Number_of_games = int(input())
game = []
for i in range(Number_of_games):
    game += [input().split(';')]
  
for i in range(Number_of_games):
    teams.add(game[i][0])
    teams.add(game[i][2])

for i in range(Number_of_games):
    total_table[game[i][0]] = [0, 0, 0, 0, 0]
    total_table[game[i][2]] = [0, 0, 0, 0, 0]
    
for i in range(Number_of_games):
    if int(game[i][1]) > int(game[i][3]):
        result = 'win'
    elif int(game[i][1]) < int(game[i][3]):
        result = 'lost'
    else:
        result = 'draw'
    total_stats = team_stat(game[i][0], result)
    for j in range(5):
        total_table[game[i][0]][j] += total_stats[j]


for i in range(Number_of_games):
    if int(game[i][1]) > int(game[i][3]):
        result = 'lost'
    elif int(game[i][1]) < int(game[i][3]):
        result = 'win'
    else:
        result = 'draw'
    total_stats = team_stat(game[i][2], result)

    for j in range(5):
        total_table[game[i][2]][j] += total_stats[j]


for key, value in total_table.items():    
    print(key + ':', end='')
    print(*value)
