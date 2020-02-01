num_people = int(input())
network = {}

for i in range(num_people-1):
    temp = int(input())
    if temp in network:
        network[temp].append(i+1)
    else:
        network[temp] = [i+1]

#print(network)

people = [int(x) for x in range(1,num_people)]

def recurse(people, removed):
    if people:
        nexttest = set()
        for i in people:
            removed.add(i)
            if network[int(i)] not in removed:
                nexttest.add(network[i])
        return(recurse(nexttest, removed))
    return(removed)

print(recurse([3], set()))


    


