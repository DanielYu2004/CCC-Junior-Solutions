
print("Enter the speed limit: ")
speedlimit = int(input())
print("Enter the recorded speed of the car: ")
carspeed = int(input())

if carspeed <= speedlimit:
    print("Congratulations, you are within the speed limit")
else:
    if carspeed - speedlimit >= 31:
        print("You are speeding and your fine is $500")
    elif carspeed - speedlimit >= 21:
        print("You are speeding and your fine is $270")
    else:
        print("You are speeding and your find is $100")