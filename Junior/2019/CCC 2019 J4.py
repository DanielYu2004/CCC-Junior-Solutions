flips = input()

hori = flips.count('H') % 2
vert = flips.count('V') % 2

if hori == 1 and vert == 1:
    print('4 3')
    print('2 1')
if hori == 1 and vert == 0:
    print('3 4')
    print('1 2')
if hori == 0 and vert == 1:
    print('2 1')
    print('4 3')
if hori == 0 and vert == 0:
    print('1 2')
    print('3 4')
#remember to try to make a one line sol