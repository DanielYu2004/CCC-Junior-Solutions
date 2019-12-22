mins = int(input())

loops = mins // 720

mins = mins % 720

a = 1
b = 2
c = 0
d = 0

sol = 0

if mins <= 720:
    for i in range(mins):
        if d < 9:
            d += 1
        else:
            d = 0
            if c < 5:
                c += 1
            else:
                c = 0
                if a == 1 and b == 2:
                    a = 0
                    b = 1
                elif b < 9:
                    b += 1
                else: 
                    b = 0
                    a = 1
        if a != 0:
            if (a-b == b-c == c-d):
                sol +=1
        elif(b-c == c-d):
                sol +=1

print(loops*31 + sol)
