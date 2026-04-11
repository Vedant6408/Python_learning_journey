#we're gonna make a program using nested statement
while True:
    a = input("Enter your number: ")
    if a.lstrip("-").isdigit():
        a = int(a)
        if(a%2)==0:
            print("Even")
            break
        else:
            print("Odd")
            break
    else:
        print("Invalid Input")
        print("Try again")
        