
numboards = int(input())

arr = [int(x) for x in input().split()]

arr = tuple(arr)
heights = []

for i in range(numboards):
  for q in range(i+1,numboards):
    heights.append(arr[i] + arr[q])

heights = list(set(heights))
solheights = [0] * len(heights)



for i in range(len(heights)):
    temparr = arr
    temparr = list(temparr)
    temparr.sort() #what the fukc why does removing .sort change anything what the fuck
    #print(i)
    while (temparr):
            #print(temparr)
        #if ((heights[i] - temparr[0]) in temparr):
            #if (temparr[1:].index(heights[i] - temparr[0])):
        #if((heights[i]-temparr[0]) in temparr[1:]):
        #if ((heights[i]-temparr[0] in temparr[1:])):
        if (heights[i] - temparr[0] in temparr[1:]):
            solheights[i] += 1    
            temparr.remove(heights[i] - temparr[0])
            del temparr[0]
        #if len(temparr) > 0:
        else:
            del temparr[0]


uniquesolheights = list(set(solheights))
occur = [0] * len(uniquesolheights)


for i in range(len(uniquesolheights)):
    occur[i] = solheights.count(uniquesolheights[i])

#print(heights)
#print(solheights)
print(max(uniquesolheights), solheights.count(max(uniquesolheights)))
