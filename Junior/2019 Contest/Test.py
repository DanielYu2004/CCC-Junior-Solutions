from math import sqrt
from math import ceil
import sys
width = int(input())
length = int(input())
#if length > 200:
#    print('yes')
#    sys.exit()
board = []
values = {}
for x in range(width):
    temp = input().split()
    board.append(temp)
    for y in range(len(temp)):
        #print(temp[y])
        if temp[y] not in values:
            values[temp[y]] = [[x,y]]
        else:
            values[temp[y]].append([x,y])
visited2 = set()
#print(values)
#print(board)
start = int(board[0][0])
end = int(width * length)

visited = set()

def possibleJumps(product):
    output = []
    for i in range(1, ceil(sqrt(product)) + 1):
        temp = product / i
        if int(temp) == temp or temp % 1 == 0:
            #print(visited)
            test1 = str(int(temp)) + " " +  str(i)
            test2 = str(i) + " " +  str(int(temp))
            if test1 not in visited:
                output.append([int(temp), i])
                #visited.add(test1)
            if test2 not in visited:
                output.append([i, int(temp)])
                #visited.add(test2)
            #if tuple([int(temp), i]) not in visited:
            #    output.append([int(temp), i])
            #    visited.add(tuple([int(temp), i])) #####rember
            #if tuple([i, int(temp)]) not in visited:
            #    output.append([i, int(temp)])
            #    visited.add(tuple([i, int(temp)])) #####rember
    #print("output" , output)
    return(output)
#print(possibleJumps(100))

def recurse(positionnum):
    global end
    global board
    global length
    #print(positionnum)
    if positionnum == end or positionnum == str(end):
        print("yes")
        sys.exit()
    #print(positionnum)
    else:
        next = possibleJumps(int(positionnum))
        #print("Next" , next)
        for i in next:
            if len(board) > i[0]-1 and length > i[1]-1: 
                if board[i[0]-1][i[1]-1] not in visited2:
                    visited2.add(board[i[0]-1][i[1]-1])

                #print(i)
                #print(board[i[0]-1][i[1]-1])
                    recurse(board[i[0]-1][i[1]-1])
recurse(int(start))
print("no")