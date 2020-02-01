numpie = int(input())
numpeople = int(input())
counter = 0


memoize = {}


def solve(people, pie, minpie):
    global counter
    #print(people)
    if (people,pie,minpie) in memoize:
        counter += memoize[(people, pie, minpie)]
    else:
        if people > 1:
            maxpie = pie // people
            tempcounter = counter
            for i in range(minpie, maxpie+1):
                #print(i)
                solve(people-1, pie - i, i)
            memoize[(people,pie,minpie)] = counter - tempcounter
        else:
            counter +=1



solve(numpeople, numpie, 1)
print(counter)