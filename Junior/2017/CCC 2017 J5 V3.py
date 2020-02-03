num_boards = int(input())

boards = [int(x) for x in input().split()]

boards = sorted(boards)

uniqueboards = sorted(list(set(boards)))

heights = {}



for x in range(len(uniqueboards)):
    for y in range(x+1, len(uniqueboards)):
        heights[uniqueboards[x]+uniqueboards[y]] = 0
    if boards.count(uniqueboards[x]) > 1:
        heights[uniqueboards[x] * 2] = 0


#print(heights)

for target in heights.keys():
    y = len(boards)-1
    x = 0
    tempboards = list(boards)
    while y > x:
        if tempboards[x] + tempboards[y] == target:
            #tempboards.pop(y)
            #y -= 2
            #tempboards.pop(x)
            x += 1
            y -= 1
            heights[target] +=1
        elif tempboards[x] + tempboards[y] > target:
            y -= 1
        elif tempboards[x] + tempboards[y] < target:
            x+=1
#print(heights)

longest = 0
num_longest = 0

for key,value in heights.items():
    if value > longest:
        num_longest = 1
        longest = value
    elif value == longest:
        num_longest +=1

print(longest, num_longest)

#print(heights)


