n = int(input())
k = int(input())

sol = 0

for i in range(k+1):
    sol = sol + n*(10**(i))

print(sol)
