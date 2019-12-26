word = input()

#print(word[::-1])

sol=0

for i in range(len(word)): #do i need to loop for len or len/s
    for p in range(len(word)):
        tempword = word[i:len(word)-p]
        #print(tempword)
        if (tempword == tempword[::-1] and len(tempword) > sol):
            sol = len(tempword)
print(sol)