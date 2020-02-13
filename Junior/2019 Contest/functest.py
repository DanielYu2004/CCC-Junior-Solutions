from math import sqrt
from math import ceil

x = int(input())
y = int(input())

end = x * y

startlist = []
boarddict = {}


for a in range(y):
    row = [int(h) for h in input().split()]
    for b in range(x):
        if row[b] == end:
            startlist.append([a,b])
print(startlist)


def recur(points):
    pass


def possibleJumps(product):
    output = []
    for i in range(1, ceil(sqrt(product)) + 1):
        temp = product / i
        if int(temp) == temp or temp % 1 == 0:
            if x > temp-1 and y > i - 1:
                output.append(temp,i)
    return(output)
    
    
#indices = [i for i, x in enumerate(my_list) if x == "whatever"]
