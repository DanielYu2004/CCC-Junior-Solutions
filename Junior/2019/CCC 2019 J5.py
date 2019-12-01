#to do list:
#need to be able to make determine paths take a multiple character rule input
#Add one more rule
#implement a parent node system 
#whilst doing steps traversal, have if statement for the final output, if found, find the parent nodes and which rules were used



#_____________________
#figure out how to use the temp lists in steps traversal 
#implement system to add nodes to find_test_nodes

#create a level counter so program knows when to stop steps_traversal
#figure out how once the program stops the left most path, it knows to go backwards and continue the program by going to the right path

rule_one_in, rule_one_out = input().split()
rule_two_in, rule_two_out = input().split()
rule_three_in, rule_three_out = input().split()
steps, start, end = input().split()
steps = int(steps)
"""
start = "AB"
rule_one_in = "AA"
rule_two_in = "AB"
rule_three_in = "B"
rule_one_out = "AB"
rule_two_out = "BB"
rule_three_out = "AA"
steps = 4
end = "AAAB"
"""
list_values = [] #may have to put this inside the function
sol = []
sol_test_list = []

def func_one(letter):
    letter = rule_one_out
    return (letter)

def func_two(letter):
    letter = rule_two_out
    return (letter)

def func_three (letter):
    letter = rule_three_out
    return (letter)

class Node:
    def __init__ (self, value):
        self.value = value
        self.child = []
        self.rule_used = None
        self.order = None
        self.parent = None
        self.index = None
        
    def determine_paths(self, cur_step): #takes a node as an input and creates all possible children of that node with the rules
        list_counter = 0 
        len_counter = 0
        #check replace function for multiple instances of the same letter
        #fix other side for replace function
        list_values = list(self.value)
        templist = []
        for i in (self.value):
            #print ("this is character: " , i)
           # print ("len counter: " , len_counter)
            if len(rule_one_in) == 1:
           #     print ("no")
                if i == rule_one_in:
                    templist = list_values[len_counter]
                    list_values[len_counter] = func_one(i)
                    self.child.append(Node("".join(list_values)))
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "1"
                    self.child[list_counter].parent = self
                    self.child[list_counter].index = len_counter + 1
                    if int(cur_step) == (int(steps) - 2):
                       # print ("TESTING:__________" , self.child[list_counter].value, " and " , str (end))
                        if self.child[list_counter].value == end:
                            self.child[list_counter].find_sol()
                    list_values = list(self.value)
                    list_values[len_counter] = templist
                    templist = []
                    list_counter += 1
                
                    
            if len_counter + len(rule_one_in) <= len(list_values):
                for r in range (len(rule_one_in)):
                    templist.append(list_values[(len_counter + r)])
              #  print ("templist: " , templist)
                if "".join(templist) == rule_one_in:
                    for e in range(len(rule_one_in)):
                        list_values.pop(len_counter)
                    list_values.insert(len_counter, rule_one_out)
                    self.child.append(Node("".join(list_values)))
                 #   print ("Node Appended")
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "1"
                    self.child[list_counter].parent = self
                    self.child[list_counter].index = len_counter + 1
                    list_values = list(self.value)
                    if int(cur_step) == (int(steps) - 2):
                        #print ("TESTING:__________" , self.child[list_counter].value, " and " , str (end))
                        if self.child[list_counter].value == end:
                            self.child[list_counter].find_sol()
                  #  print ("list values: ", list(self.value))
                    #list_values[len_counter] = templist
                    list_counter += 1
                templist = []

            if len(rule_two_in) == 1:
                if i == rule_two_in:
                    templist = list_values[len_counter]
                    list_values[len_counter] = func_two(i)
                    self.child.append(Node("".join(list_values)))
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "2"
                    self.child[list_counter].parent = self
                    self.child[list_counter].index = len_counter + 1
                    if int(cur_step) == (int(steps) - 2):
                       # print ("TESTING:__________" , self.child[list_counter].value, " and " , str (end))
                        if self.child[list_counter].value == end:
                            self.child[list_counter].find_sol()
                    list_values = list(self.value)
                    list_values[len_counter] = templist
                    templist = []
                    list_counter += 1
                   
                    
            if len_counter + len(rule_two_in) <= len(list_values):
                for r in range (len(rule_two_in)):
                    templist.append(list_values[(len_counter + r)])
               # print ("templist: " , templist)
                #print ("list values: " , list_values)
                if "".join(templist) == rule_two_in:
                    for e in range(len(rule_two_in)):
                        list_values.pop(len_counter)
                    list_values.insert(len_counter, rule_two_out)
                    self.child.append(Node("".join(list_values)))
                   # print ("Node Appended")
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "2"
                    self.child[list_counter].parent = self
                    self.child[list_counter].index = len_counter + 1
                    if int(cur_step) == (int(steps) - 2):
                       # print ("TESTING:__________" , self.child[list_counter].value, " and " , str (end))
                        if self.child[list_counter].value == end:
                            self.child[list_counter].find_sol()
                    list_values = list(self.value)
                  #  print ("list values: ", list(self.value))
                    #list_values[len_counter] = templist
                    list_counter += 1
                templist = []

                
            if len(rule_three_in) == 1:
           #     print ("no")
                if i == rule_three_in:
                    templist = list_values[len_counter]
                    list_values[len_counter] = func_one(i)
                    self.child.append(Node("".join(list_values)))
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "3"
                    self.child[list_counter].parent = self
                    self.child[list_counter].index = len_counter + 1
                    if int(cur_step) == (int(steps) - 2):
                      #  print ("TESTING:__________" , self.child[list_counter].value, " and " , str (end))
                        if self.child[list_counter].value == end:
                            self.child[list_counter].find_sol()
                    list_values = list(self.value)
                    list_values[len_counter] = templist
                    templist = []
                    list_counter += 1

                    
            if len_counter + len(rule_three_in) <= len(list_values):
                for r in range (len(rule_three_in)):
                    templist.append(list_values[(len_counter + r)])
              #  print ("templist: " , templist)
                if "".join(templist) == rule_three_in:
                    for e in range(len(rule_three_in)):
                        list_values.pop(len_counter)
                    list_values.insert(len_counter, rule_three_out)
                    self.child.append(Node("".join(list_values)))
                 #   print ("Node Appended")
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "3"
                    self.child[list_counter].parent = self
                    self.child[list_counter].index = len_counter + 1
                    if int(cur_step) == (int(steps) - 2):
                      #  print ("TESTING:__________" , self.child[list_counter].value, " and " , str (end))
                        if self.child[list_counter].value == end:
                            self.child[list_counter].find_sol()
                    list_values = list(self.value)
                  #  print ("list values: ", list(self.value))
                    #list_values[len_counter] = templist
                    list_counter += 1
                templist = []

            len_counter += 1


    def find_sol (self):
        sol_test_list.append(self)
        for j in range (steps):
            sol_test_list[j].get_info()
            
        for p in range(len(sol)):
            print (sol[len(sol)-p-1][0], " " , sol[len(sol)-p-1][1], " " , sol[len(sol)-p-1][2])
        exit()
        

    def get_info(self):
        if self.parent:
            temp_sol_list = []
            temp_sol_list.append(self.rule_used)
            temp_sol_list.append(self.index)
            temp_sol_list.append(self.value)
            sol.append(temp_sol_list)
            sol_test_list.append(self.parent)
            










        







            
            """
            if len(rule_two_in) == 1:
                if i == rule_two_in:
                    templist = list_values[len_counter]
                    list_values[len_counter] = func_two(i)
                    self.child.append(Node("".join(list_values)))
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "rule two"
                    list_values = list(self.value)
                    list_values[len_counter] = templist
                    templist = []
                    list_counter += 1

                    
            if len_counter + len(rule_two_in) <= len(list_values):
                for r in range (len(rule_two_in)):
                    templist.append(list_values[(len_counter + r)])
                if "".join(templist) == rule_two_in:
                    for e in range(len(rule_two_in)):
                        list_values.pop(len_counter + e)
                    list_values.insert(len_counter, rule_two_out)
                    self.child.append(Node("".join(list_values)))
                    self.child[list_counter].order = list_counter + 1
                    self.child[list_counter].rule_used = "rule two"
                    list_values = list(self.value)
                    #list_values[len_counter] = templist
                    templist = []
                    list_counter += 1
                    """
            """
            if i == rule_two_in:
                templist = list_values[len_counter]
                list_values[len_counter] = func_two(i)
                self.child.append(Node("".join(list_values)))
                self.child[list_counter].order = list_counter + 1
                self.child[list_counter].rule_used = "rule two"
                list_values = list(self.value)
                list_values[len_counter] = templist
                templist = None
                list_counter += 1
            len_counter += 1
            #remember to make a function for rules rather than if statem ents for each one  
                    """
            
    def steps_traversal(self): #will use the determine paths function and create x number of layers of the tree
                            #remember to not include if statement to check for final output in this function because we need to execute the entire function and only the check the leafs of the tree


           # print ("1:")
            self.determine_paths(1)
            find_test_nodes = [] #have to change this if expanding number of rules or changing the rules since not all rules will be always used.
            for m in range (len(self.child)):
                find_test_nodes.append(self.child[m])
              #  print (self.child[m].value)
            test_nodes = []
            for i in range(steps-1):
                #print (i + 2, ":")
                for q in range (len(find_test_nodes)):
                    if not find_test_nodes[q] == 0:
                        test_nodes.append(find_test_nodes[q])
                        find_test_nodes[q] = 0
                for e in range (len(test_nodes)):
                    test_nodes[e].determine_paths(i)
                    for p in range (len(test_nodes[e].child)):
                      #  print (test_nodes[e].child[p].value)
                        find_test_nodes.append(test_nodes[e].child[p])
                test_nodes.clear()

class Tree:
    def __init__ (self, value):
        self.root = Node(value)

tree = Tree(start)
tree.root.steps_traversal()

#print (len(tree.root.child[0].child[0].child))














