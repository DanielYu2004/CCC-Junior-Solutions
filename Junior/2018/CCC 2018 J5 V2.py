#woohoo perfect score this time


class Page:
    def __init__(self, value):
        self.value = value
        self.children = []

def findreachable(node, reachedpages):
    if (node.value not in reachedpages):
        reachedpages.append(node.value)
#        print(len(reachedpages))
        #print(node)
        for i in node.children:
            findreachable(i, reachedpages)

def traversal (nodes, visited, level):
    level += 1
    queue = []
    for node in nodes:

        if node not in visited:
            visited.append(node)
            #print("node:" , node.value)
            
            if node.children:
                for x in node.children:
                    queue.append(x)
            else:
                print(level)
                return()

    traversal(queue, visited, level)















    #level+=1
    #if (node not in visited):
    #    visited.append(node)
    #    print(node.value)
    #    for i in node.children:
    #        templevel = level
    #        return(traversal(i, visited, templevel))
    #return(level)





num_pages = int(input())

book = {}

for i in range(1,num_pages+1):
    book[i] = Page(i)


for i in range(1,num_pages+1):
    temp = [int(x) for x in input().split()]
    for q in (temp[1:]):
        book[i].children.append(book[q])


reachedpages = []

findreachable(book[1], reachedpages)

#print(reachedpages)
if (len(reachedpages) == num_pages):
    print("Y")
else:
    print("N")

level = 0
visited = []
traversal([book[1]], visited, level)






