ruleone = input().split()
ruletwo = input().split()
rulethree = input().split()


def applyrules(string):
    output = []

    for i in range(len(string)):
        if len(string) - i >= len(ruleone[0]):
            if string[i:len(ruleone[0])+i] == ruleone[0]:
                output.append([string[0:i] + ruleone[1] + string[i+len(ruleone[0]):], i, "1"])

    for i in range(len(string)):
        if len(string) - i >= len(ruletwo[0]):
            if string[i:len(ruletwo[0])+i] == ruletwo[0]:
                output.append([string[0:i] + ruletwo[1] + string[i+len(ruletwo[0]):], i, "2"])

    for i in range(len(string)):
        if len(string) - i >= len(rulethree[0]):
            if string[i:len(rulethree[0])+i] == rulethree[0]:
                output.append([string[0:i] + rulethree[1] + string[i+len(rulethree[0]):], i, "3"])
    return(output)


inputs = input().split()
steps = int(inputs[0])
initial = inputs[1]
end = inputs[2]


class Node:
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.children = {}
        self.path = []


    def determine_paths(self, nodes, level):
        if level < steps:
            level +=1
            queue = []
            for node in nodes:
                
                for i in(applyrules(node.value)): #remember to consider repeat strings -> make a hashmap of already created nodes
                    #print(i)
                    temp = Node(i[0], level)
                    node.children[temp] = [i[1], i[2]]#this doesn't have to be dictionary
                    temp.path = node.path
                    temp.path = temp.path + [i[2], i[1], temp.value]
                    queue.append(temp)
                    #print(temp.value)
            self.determine_paths(queue, level)

#    def bfs(self, nodes, visited):
#        queue = []
#        for node in nodes:
#            if node not in visited:
#                visited.append(node)
#                if node.value == end and node.level == steps:
##                    return(node)
#                queue.append(node)  
#        return()

    def dfs(self, node):
        if str(node.value) == str(end) and int(node.level) == steps:
            repeat = len(node.path)/3
            for i in range(int(repeat)):
                print(node.path[i*3], (node.path[(i*3)+1])+1, node.path[(i*3)+2])
            exit()


        for i in node.children.keys():
            self.dfs(i)
            

            

root = Node(initial, 0)
root.determine_paths([root], 0)
root.dfs(root)
