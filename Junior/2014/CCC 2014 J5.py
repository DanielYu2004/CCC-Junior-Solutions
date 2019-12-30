num = int(input())

names1 = [str(x) for x in input().split()]
names2 = [str(x) for x in input().split()]

dict1 = {}
dict2 = {}

for i in range(num):
    
    dict1[names1[i]] = names2[i]
    dict2[names2[i]] = names1[i]


for i in range(num):
    if (dict1[names1[i]] != dict2[names1[i]]) or (names1[i] == dict1[names1[i]]) or (dict2[names2[i]] == names2[i]):
        print("bad") 
        exit()

print("good")
