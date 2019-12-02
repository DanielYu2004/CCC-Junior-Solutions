rows = int(input())
arr = []
sol = []

for i in range(rows):
    arr.append(input().split())

#print(arr)
for i in range(len(arr)):

    sol.append(str(arr[i][1]) * int(arr[i][0]))

#print(sol)
for i in range(len(sol)):
    print(sol[i])
