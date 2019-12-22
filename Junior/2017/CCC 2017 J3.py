start = input().split()
end = input().split()
energy = int(input())

xdif = int(start[0]) - int(end[0])
ydif = int(start[1]) - int(end[1])

if (ydif + xdif > energy):
    print("N")
elif (xdif+ydif == energy or (energy - (xdif + ydif))%2 == 0):
    print("Y")
else:
    print("N")