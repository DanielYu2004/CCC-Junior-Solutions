arr1 = [int(x) for x in input().split()]

arr2 = [int(x) for x in input().split()]
arr3 = [int(x) for x in input().split()]
arr4 = [int(x) for x in input().split()]
arr = [arr1, arr2, arr3, arr4]

mag = 0

for i in arr1:
    mag += int(i)

for i in range(4):
    if arr[i][0] + arr[i][1] + arr[i][2] + arr[i][3] != mag:
        mag = 0

for i in range(4):
    if arr[1][i] + arr[2][i] + arr[3][i] + arr[0][i] != mag:
        mag = 0

if mag:
    print("magic")
else:
    print("not magic")  

