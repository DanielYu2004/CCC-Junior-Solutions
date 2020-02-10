message = str(input())

happy = message.count(":-)")
sad = message.count(":-(")

if happy > sad:
    print("happy")
elif happy == sad and happy !=0:
    print("unsure")
elif happy == 0 and sad == 0:
    print("none")
else:
    print("sad")