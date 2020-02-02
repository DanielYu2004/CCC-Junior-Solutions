favteam = int(input())

numgames = int(input())

playedgames = []

for i in range(numgames):
    playedgames.append([int(x) for x in input().split()])

scores = {
    1:0,
    2:0,
    3:0,
    4:0,
}

played = {
    (1,2):False,
    (1,3):False,
    (1,4):False,
    (2,3):False,
    (2,4):False,
    (3,4):False,
}
#print(playedgames)
for i in range(len(playedgames)):

    if playedgames[i][2] > playedgames[i][3]:
        scores[playedgames[i][0]] += 3
    elif  playedgames[i][2] <  playedgames[i][3]:
        scores[ playedgames[i][1]] += 3
    else:
        scores[ playedgames[i][0]] += 1
        scores[ playedgames[i][1]] += 1
    played[(playedgames[i][0], playedgames[i][1])] = True

#print(scores)
#print(played)
 

gamesleft = []

for i in played.keys():
    if played[i] == False:
        gamesleft.append(i)

#print(gamesleft)

wins = 0

def solve(games, scores):
    global favteam
    global wins
    if len(games) > 0:
        teams = []
        for x in games[0]:
            teams.append(x)
        
        for i in range(1,4):
            hyposcores = dict(scores)
            if i == 1:
                hyposcores[teams[0]] += 3
                #print("hypo",hyposcores)
                solve(games[1:],hyposcores)
            if i == 2:
                hyposcores[teams[1]] += 3
                #print("hypo",hyposcores)
                solve(games[1:],hyposcores)
            if i == 3:                
                hyposcores[teams[0]] += 1
                hyposcores[teams[1]] += 1
                #print("hypo",hyposcores)
                solve(games[1:],hyposcores)

    else:
        #print("scores" , scores)
        winner = True
        for i in scores.keys():
            if i != favteam:
                if scores[favteam] <= scores[i]:
                    winner = False
                    break
        if winner == True:
            #print(scores)
            wins += 1





solve(gamesleft, dict(scores))
print(wins)


