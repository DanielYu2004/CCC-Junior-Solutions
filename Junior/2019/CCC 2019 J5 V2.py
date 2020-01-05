ruleone = input().split()
ruletwo = input().split()
rulethree = input().split()


def applyrules(string):
    output = []

    for i in range(len(string)):
        if len(string) - i >= len(ruleone[0]):
            if string[i:len(ruleone[0])+i] == ruleone[0]:
                output.append([string[0:i] + ruleone[1] + string[i+len(ruleone[0]):], i, "ruleone"])

    for i in range(len(string)):
        if len(string) - i >= len(ruletwo[0]):
            if string[i:len(ruletwo[0])+i] == ruletwo[0]:
                output.append([string[0:i] + ruletwo[1] + string[i+len(ruletwo[0]):], i, "ruletwo"])

    for i in range(len(string)):
        if len(string) - i >= len(rulethree[0]):
            if string[i:len(rulethree[0])+i] == rulethree[0]:
                output.append([string[0:i] + rulethree[1] + string[i+len(rulethree[0]):], i, "rulethree"])
    return(output)


inputs = input().split()
steps = inputs[0]
initial = inputs[1]
end = inputs[2]


class Node:
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.children = {}


    def determine_paths(self, nodes, level):
        level +=1
        queue = []
        for node in nodes:
            
            for i in(applyrules(node.value)): #remember to consider repeat strings -> make a hashmap of already created nodes
                print(i)
                temp = Node(i[0], level)
                node.children[temp.value] = [i[1], i[2]]
                queue.append(temp)
                print(temp.value)
        self.determine_paths(queue, level)



        return()

root = Node(initial, 0)
root.determine_paths([root], 0)
#print(applyrules(initial))