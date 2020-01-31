
testcases = []
a = 1
while a != 0:
    temp = [ int(x) for x in input().split() ]
    #print(temp)
    if temp[0] == 0:
        a = 0
    else:
        testcases.append(temp[1:])

def finddifs(nums):
    temp = []
    for i in range(len(nums)-1):
        temp.append(nums[i+1]-nums[i])
    return(temp)

for i in range(len(testcases)):
    testcases[i] = finddifs(testcases[i])


def findpattern(nums):
    length = len(nums)

    for i in range(length):
        testpattern = nums[0:i+1]
        found = True
        for i in range(len(nums)):
            if not nums[i] == testpattern[ i % len(testpattern) ]:
                found = False
        if found == True:
            if not testpattern:
                return(1)
            return(len(testpattern))
    if nums == []:
        return(0)


for i in testcases:
    print(findpattern(i))