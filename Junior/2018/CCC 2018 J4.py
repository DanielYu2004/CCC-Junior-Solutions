length = int(input())
grid = []
for i in range (length):
    grid.append(input().split())


def rotate(grid):
    list = []
    templist = []
    for q in range (length):
        for e in range (length):
            templist.append(grid[length-e-1][q])
        list.append(templist)
        templist = []
    return list

def check (grid):
    #print (grid)
    check = True
    for i in range (length):
        for e in range (length-1):
            #print (grid[i][e] , grid[i][e+1])
            if int(grid[i][e]) >= int(grid[i][e+1]):
                check = False
    for q in range (length-1):
        if int(grid[q][0]) >= int(grid[q+1][0]):
            check = False
    if check == True:
        for i in range(length):
            for e in range (length):
                print (grid[i][e], end = ' ')
            print ("")
    #    exit()