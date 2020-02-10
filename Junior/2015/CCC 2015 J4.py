num_messages = int(input())

messages = []
people = {}
for i in range(num_messages):
    temp = input().split()
    if temp[0] != 'W':
        people[temp[1]] = {
            'reply' : False,
            'waittime' : 0,
            'lastmessage' : 0
        }
    messages.append(temp)

#print(messages)
#print(people)

counter = 0
for i in range(len(messages)):
    if messages[i][0] == 'W':
        counter += (int(messages[i][1]) - 1)
    else:
        counter +=1

    if messages[i][0] == 'R':
        people[messages[i][1]]['reply'] = True 
        people[messages[i][1]]['lastmessage'] = counter 

    if messages[i][0] == 'S':
        people[messages[i][1]]['reply'] = False 
        people[messages[i][1]]['waittime'] += counter - people[messages[i][1]]['lastmessage']
sol = []
for key in people.keys():
    if people[key]['reply'] == True:
        sol.append([key, '-1'])
    else:
        sol.append([key , people[key]['waittime']])

#print(sol)
smallest = 10000000000
temp = 0
while sol:
    for i in range(len(sol)):
        if int(sol[i][0]) < smallest:
            smallest = int(sol[i][0])
            temp = i
    smallest = 10000000000000
    print(sol[temp][0], sol[temp][1])
    sol.pop(temp)
