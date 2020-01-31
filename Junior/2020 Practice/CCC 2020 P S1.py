num_games = int(input())

team1 =  [ int(x) for x in input().split()]
team2 =  [ int(x) for x in input().split()]

largest = 0
team1sum = 0
team2sum = 0
for i in range(num_games):
    team1sum += team1[i]
    team2sum += team2[i]

    if team1sum == team2sum:
        largest = i + 1

print(largest)
