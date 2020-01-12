numboards = int(input())

boards = [int(x) for x in input().split()]

uniqueboards = list(set(boards)) #all different types of single board heights
boards = tuple(sorted(boards))
boardsdict = {}#all possible total heights of fences and how many times two boards can be combined to make them

if len(uniqueboards) == 1:
    boardsdict[uniqueboards[0]*2] = 0
else:
    for x in range(len(uniqueboards)):
        for i in range(x+1, len(uniqueboards)):
            boardsdict[uniqueboards[x] + uniqueboards[i]] = 0

def pairboards(boards, target):
    global boardsdict
    tempboards = list(boards)
    x = 0
    while tempboards:
        if x >= len(tempboards):
            break
        if target - tempboards[x] in tempboards[(x+1)::]:
            temp = tempboards[x]
            del tempboards[x]
            tempboards.remove(target-temp)
            boardsdict[target] += 1
        else:
            x+=1

for x in boardsdict.keys():
    pairboards(boards, x)


modesdict = {}

for x in boardsdict.values():
    if x not in modesdict:
        modesdict[x] = 1
    else:
        modesdict[x] +=1

longest = 0
numberofhighestmodes = 0

for key, value in modesdict.items():
    if key > longest:
        longest = key
        numberofhighestmodes = value

print(longest, numberofhighestmodes)

    



