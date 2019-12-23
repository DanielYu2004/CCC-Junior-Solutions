arr = [0] * 6

for i in range(6):
    arr[i] = input()

if arr.count("W") == 5 or arr.count("W") == 6:
    print("1")
elif arr.count("W") == 4 or arr.count("W") == 3:
    print("2")
elif arr.count("W") == 2 or arr.count("W") == 1:
    print("3")
else:
    print("-1")