ruleone = input().split()
ruletwo = input().split()
rulethree = input().split()


def applyrules(string):
    output = []
    global visited
    for i in range(len(string)):
        if len(string) - i >= len(ruleone[0]):
            if string[i:len(ruleone[0])+i] == ruleone[0]:
                if [string[0:i] + ruleone[1] + string[i+len(ruleone[0]):] not in visited:
                    output.append([string[0:i] + ruleone[1] + string[i+len(ruleone[0]):], i, "1"])

    for i in range(len(string)):
        if len(string) - i >= len(ruletwo[0]):
            if string[i:len(ruletwo[0])+i] == ruletwo[0]:
                if [string[0:i] + ruletwo[1] + string[i+len(ruletwo[0]):] not in visited:
                    output.append([string[0:i] + ruletwo[1] + string[i+len(ruletwo[0]):], i, "2"])

    for i in range(len(string)):
        if len(string) - i >= len(rulethree[0]):
            if string[i:len(rulethree[0])+i] == rulethree[0]:
                if [string[0:i] + rulethree[1] + string[i+len(rulethree[0]):] not in visited:
                    output.append([string[0:i] + rulethree[1] + string[i+len(rulethree[0]):], i, "3"])
    return(output)


inputs = input().split()
steps = int(inputs[0])
initial = inputs[1]
end = inputs[2]

visited = {}

class Node:
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.path = []


    def dfs(self, node, level):
        global visited
        if level < steps:
            level+=1
            if node.value not in visited:
                visited[node.value] = applyrules(node.value)
            for i in visited[node.value]:
                temp = Node(i[0], level)
                temp.path = node.path + [i[2], i[1], temp.value]

                if temp.value == end:
                    repeat = len(temp.path)/3
                    for i in range(int(repeat)):
                        print(temp.path[i*3], (temp.path[(i*3)+1])+1, temp.path[(i*3)+2])
                    exit()
                
                self.dfs(temp, level)

root = Node(initial, 0)
root.dfs(root, 0)

