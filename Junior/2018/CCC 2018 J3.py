arr = input().split()

#this was the fastest sol i could think of

print('0', int(arr[0]) , int(arr[0]) + int(arr[1]), int(arr[0]) + int(arr[1]) + int(arr[2]), int(arr[0]) + int(arr[1]) + int(arr[2]) + int(arr[3]))
print(int(arr[0]), '0', int(arr[1]), int(arr[1]) + int(arr[2]), int(arr[1]) + int(arr[2]) + int(arr[3]))
print(int(arr[0]) + int(arr[1]), int(arr[1]), '0', int(arr[2]), int(arr[2])+int(arr[3]))
print(int(arr[0]) + int(arr[1]) + int(arr[2]), int(arr[1]) + int(arr[2]), int(arr[2]), '0', int(arr[3]))
print(int(arr[0]) + int(arr[1]) + int(arr[2]) + int(arr[3]), int(arr[1]) + int(arr[2]) + int(arr[3]),int(arr[2]) + int(arr[3]), int(arr[3]), '0')
