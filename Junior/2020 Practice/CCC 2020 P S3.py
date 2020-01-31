sensors = int(input())

readings = {}

for i in range(sensors):
    temp = int(input())

    if temp in readings.keys():
        readings[temp] +=1
    else:
        readings[temp] = 1


largest = 1
second_largest = 1
first_keys = []
second_keys = []
for i in (readings.keys()):
    if readings[i] > largest:
        second_largest = largest
        largest = readings[i]
        second_keys = first_keys
        first_keys = [i]
    elif readings[i] == largest:
        first_keys.append(i)
    elif readings[i] > second_largest:
        second_largest = readings[i]
        second_keys = [i]
    elif readings[i] == second_largest:
        second_keys.append(i)



    
#print("first:" , first_keys)
#print("second:" ,second_keys)

if len(first_keys) == 1:
    if abs(first_keys[0] - min(second_keys)) > abs(first_keys[0] - max(second_keys)):
        print(abs(first_keys[0] - min(second_keys)))
    else:
        print(abs(first_keys[0] - max(second_keys)))
else:
    print(abs(max(first_keys) - min(first_keys)))


    


    