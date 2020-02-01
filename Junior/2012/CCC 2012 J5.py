import copy

initialcases = []
checked = {}
a = False
while a == False:
    trash = int(input())
    if trash == 0:
        a = True
    else:
        case = [[int (x)] for x in input().split()]
        initialcases.append(case)
    

def findsol(positions, level):
    global checked

    #print("hi")
    nextpositions = []
    for position in positions:
        if " ".join(map(str, position)) not in checked:
            solution = True
            prevcoin = 0
            for coin in position:
                if len(coin) == 1 and coin[0] > prevcoin:
                    prevcoin = coin[0]
                else:
                    solution = False
                    break
            if solution == True:
                #print("SOLUTION" , position)
                return(level)

            nextpositions += findmoves(position)
    level +=1
    if nextpositions:
        return(findsol(nextpositions, level))
    
    return("IMPOSSIBLE")



def findmoves (position):
    global checked
    moves = []
    if position:
        if " ".join(map(str, position)) not in checked:
            for spot in range(len(position)):
                for otherspot in range(len(position)):
                    if abs(spot-otherspot) == 1: #remember to just change the for loop to check if the other spot is adjacent
                        if otherspot != spot:
                            #print(position[otherspot])
                            if position[spot] and position[otherspot]:
                                if position[otherspot][0] > position[spot][0]:
                                    temp = copy.deepcopy(position)
                                    temp[spot].pop(0)
                                    #print(temp)
                                    #print(position)
                                    temp[otherspot].insert(0,position[spot][0])
                                    #print(position)
                                    #print(temp)
                                    if " ".join(map(str, temp)) not in checked:
                                        moves.append(temp)
                            elif position[spot]:
                                    temp = copy.deepcopy(position)
                                    temp[spot].pop(0)
                                    #print(temp)
                                    #print(position)
                                    temp[otherspot].insert(0,position[spot][0])
                                    #print(position)
                                    #print(temp)
                                    if " ".join(map(str, temp)) not in checked:
                                        moves.append(temp)



            checked[" ".join(map(str, position))] = moves

            return(moves)
        else:
            return(checked[" ".join(map(str, position))])

                                


    

    

for case in initialcases:
    print(findsol([case], 0))
    #sol = findsol([case], 0)
    #if sol == None:
    #    print('IMPOSSIBLE')
    #else:
    #    print(sol)
    #print(checked)
    #print(case)
    #print(findmoves(case))

"""
import copy

initialcases = []

a = False
while a == False:
    trash = int(input())
    if trash == 0:
        a = True
    else:
        case = [[int (x)] for x in input().split()]
        initialcases.append(case)
    
checked = {}
smallest = 0
def findsol(positions, level):
    global checked
    global smallest 
    #print("hi")
    nextpositions = []
    for position in positions:
        if " ".join(map(str, position)) not in checked:
            solution = True
            prevcoin = 0
            for coin in position:
                if len(coin) == 1 and coin[0] > prevcoin:
                    prevcoin = coin[0]
                else:
                    solution = False
                    break
            if solution == True:
                #print("SOLUTION" , position)
                if level > smallest:
                    smallest = level
                return(level)

            nextpositions += findmoves(position)

    level +=1
    if nextpositions:
        return(findsol(nextpositions, level))
    else:
        return()



def findmoves (position):
    global checked
    moves = []
    if position:
        if " ".join(map(str, position)) not in checked:
            for spot in range(len(position)):
                for otherspot in range(len(position)):
                    if abs(spot-otherspot) == 1: #remember to just change the for loop to check if the other spot is adjacent
                        if otherspot != spot:
                            #print(position[otherspot])
                            if position[spot] and position[otherspot]:
                                if position[otherspot][0] > position[spot][0]:
                                    temp = copy.deepcopy(position)
                                    temp[spot].pop(0)
                                    #print(temp)
                                    #print(position)
                                    temp[otherspot].insert(0,position[spot][0])
                                    #print(position)
                                    #print(temp)
                                    if " ".join(map(str, temp)) not in checked:
                                        moves.append(temp)
                            elif position[spot]:
                                    temp = copy.deepcopy(position)
                                    temp[spot].pop(0)
                                    #print(temp)
                                    #print(position)
                                    temp[otherspot].insert(0,position[spot][0])
                                    #print(position)
                                    #print(temp)
                                    if " ".join(map(str, temp)) not in checked:
                                        moves.append(temp)



            checked[" ".join(map(str, position))] = moves
            #print(moves)
            return(moves)
        else:
            return(checked[" ".join(map(str, position))])

                                


    

    

for case in initialcases:
    sol = findsol([case], 0)
    if sol == None:
        print('IMPOSSIBLE')
    else:
        print(smallest)
    #print(case)
    #print(findmoves(case))
"""