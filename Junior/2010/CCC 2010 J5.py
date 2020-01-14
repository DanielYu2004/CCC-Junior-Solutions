start = [int(x) for x in (input().split())]
end = [int(x) for x in (input().split())]

visited = set()

def find_moves(positions, level):
    next_positions = []
    #print(level)

    for temp in positions:
        x = temp[0]
        y = temp[1]
        #print(temp)
        if temp == end:
            return(level)
        if 0 < x + 2 <= 8 and 0 < y + 1 <= 8:
            if tuple([x+2,y+1]) not in visited:
                next_positions.append([x+2,y+1])
                visited.add(tuple([x+2,y+1]))
        if 0 < x + 2 <= 8 and 0 < y - 1 <= 8:
            if tuple([x+2,y-1]) not in visited:
                next_positions.append([x+2,y-1])
                visited.add(tuple([x+2,y-1]))
        if 0 < x - 2 <= 8 and 0 < y + 1 <= 8:
            if tuple([x-2,y+1]) not in visited:
                next_positions.append([x-2,y+1])
                visited.add(tuple([x-2,y+1]))
        if 0 < x - 2 <= 8 and 0 < y - 1 <= 8:
            if tuple([x-2,y-1]) not in visited:
                next_positions.append([x-2,y-1])
                visited.add(tuple([x-2,y-1]))
        if 0 < y + 2 <= 8 and 0 < x + 1 <= 8:
            if tuple([x+1,y+2]) not in visited:
                #print("FUCKKKK", x, y)
                next_positions.append([x+1,y+2])
                visited.add(tuple([x+1,y+2]))
        if 0 < y + 2 <= 8 and 0 < x - 1 <= 8:
            if tuple([x-1, y+2]) not in visited:
                next_positions.append([x-1, y+2])
                visited.add(tuple([x-1, y+2]))
        if 0 < y - 2 <= 8 and 0 < x + 1 <= 8:
            if tuple([x+1, y-2]) not in visited:
                next_positions.append([x+1, y-2])
                visited.add(tuple([x+1, y-2]))
        if 0 < y - 2 <= 8 and 0 < x - 1 <= 8:
            if tuple([x-1, y-2]) not in visited:
                next_positions.append([x-1, y-2])
                visited.add(tuple([x-1, y-2]))
#    print("VISITED", visited)
#    print("FUCK",next_positions)
    level +=1

    return(find_moves(next_positions, level))

print(find_moves([start], 0))