type = int(input())
numpairs = int(input())

ds = [int(x) for x in input().split()]

ps = [int(x) for x in input().split()]

if type == 1:

    ds.sort()
    ps.sort()

    totalspeed = 0

    for i in range(numpairs):
        totalspeed += max(ds[i],ps[i])

    print(totalspeed)
else:
    ds.sort()
    ps.sort()

    totalspeed = 0

    for i in range(numpairs):
        totalspeed += max(ds[::-1][i],ps[i])

    print(totalspeed)