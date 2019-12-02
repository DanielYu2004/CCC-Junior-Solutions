spaces = int(input())

first = input()
second = input()
counter = 0
for i in range(spaces):
    if first[i] == 'C' and second[i] == 'C':
        counter +=1

print(counter)
