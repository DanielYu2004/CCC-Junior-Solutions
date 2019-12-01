row = int(input())
arr = []

for i in range(row):
    arr.append(input())

#print (arr)
sol = []

for i in range(len(arr)):
    counter = 1
    tempsol = []
    for q in range(len(arr[i])):
        #print(q)
        pointer = arr[i][q]

        if q+1 >= len(arr[i]):
            temp = [str(counter) +  " " + str(pointer) + " "]
            tempsol +=(temp)
        
        elif pointer == arr[i][q+1]:
            counter +=1
        else:
            temp = [str(counter) +  " " + str(pointer) + " "]
            counter = 1
            tempsol +=(temp)
    sol.append(''.join(tempsol))

for i in range(len(sol)):
    print(sol[i])

        
        
            
