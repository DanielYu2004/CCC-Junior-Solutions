time = input() #try converting all units to minutes next time

hours = int(time[0:2])
minutes = int(time[3:5])

def findtime(starthour, startmin, endhour, endmin):
    if endmin == 0:
        endmin = 60
    mindif = endmin-startmin
    if endhour < starthour:
        hourdif = 24-starthour + endhour
    else:
        hourdif =endhour - starthour
    if mindif:
        hourdif -= 1
    if hourdif <0:
        hourdif = 24+hourdif
    if mindif <0:
        mindif = 60+mindif
    return(hourdif*60 + mindif)


def addtime(starthour, startmin, addmin):
    #print(addmin)
    addhour = addmin // 60
    addmin = addmin % 60
    #print(addhour)
    #print(addmin)
    startmin += addmin
    if startmin >59:
        starthour +=1
        startmin -= 60
    starthour += addhour
    if starthour >23:
        starthour -=24

    if len(str(starthour)) == 1:
        starthour = str(0) + str(int(starthour))

    else:
        starthour = int(starthour)
    if len(str(startmin)) == 1:
        startmin = str(0) + str(int(startmin))
    else:
        startmin = int(startmin)
    print(str(starthour) + ":" + str(startmin))




if hours < 5:
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)
    print("0" + str(hours+2) +":" +str(minutes) )

elif hours == 5 or hours == 6:
    traffictime = 120-findtime(hours,minutes, 7,0)
    #print(traffictime)
    addtime(hours, minutes, (traffictime + 120))

elif hours in [7,8,9]:
    traffictime = findtime(hours,minutes, 10,0)
    addtime(hours,minutes, (120-(traffictime/2) + traffictime))

elif hours < 13:
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)
    print(str(hours+2) +":" +str(minutes) )


elif hours == 13 or hours == 14:
    traffictime = 120-findtime(hours,minutes, 15,0)
    print(traffictime)
    addtime(hours, minutes, (traffictime + 120))

elif hours in [15,16,17,18]:
    traffictime = findtime(hours,minutes, 19,0)
    addtime(hours,minutes, (120-(traffictime/2) + traffictime))
elif hours in [19,20,21]:
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)
    print(str(hours+2) +":" +str(minutes) )

else:
    temphour = "0" + str((hours+2) % 24)
    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)
    
    print(temphour + ":" + str(minutes))
