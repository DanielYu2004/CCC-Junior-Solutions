message = str(input())

wordmap = {
    'b' : 'a',
    'c' : 'a',
    'd' : 'e',
    'f' : 'e',
    'g' : 'e',
    'h' : 'i',
    'j' : 'i',
    'k' : 'i',
    'l' : 'i',
    'm' : 'o',
    'n' : 'o',
    'p' : 'o',
    'q' : 'o',
    'r' : 'o',
    's' : 'u',
    't' : 'u',
    'v' : 'u',
    'w' : 'u',
    'x' : 'u',
    'y' : 'u',
    'z' : 'u'  
}
vowels = ['a','e','i','o','u']
alphabet = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
tempmessage = ''
for i in range(len(message)):
    #print("letter:", message[i])
    if message[i] not in vowels and message[i] != 'z':
        #print(message[:i] + message[i] + wordmap[message[i]] + alphabet[alphabet.index(message[i]) + 1] + message[i + 1:])
        tempmessage = tempmessage + message[i] + wordmap[message[i]] + alphabet[alphabet.index(message[i]) + 1] 
    elif message[i] in vowels:
        tempmessage = tempmessage + message[i]
        #print(tempmessage)
    else:
        tempmessage = tempmessage + message[i] + wordmap[message[i]] + 'z' 


print(tempmessage)