#first try using only if-else statement
# a = int(input("Enter your number: "))
# if a < 0:
#     print("Negative Number")
# elif a == 0:
#     print("It's a zero")
# elif a > 0:
#     print("Positive Number")
# else:
#     print("Invalid input")


#second try using while loop but there is also usage of if-else statement
# #in this written code if user type string then it will show the error
# b = int(input("Enter your number: "))
# while True:
#     if b < 0:
#         print("Negative Number")
#         break
#     elif b == 0:
#         print("It's a zero")
#         break
#     elif b > 0:
#         print("Positive Number")
#         break
#     else:
#         print("Invalid input")
#         print("Try again !")
#         b = int(input("Enter your number: "))

#we can handle that type of error using nested statement of if-else
while True:
    c = input("Enter Your Number: ")
    if c.lstrip("-").isdigit():
        c = int(c)
        if c < 0:
            print("Negative number.")
        elif c == 0:
            print("it's a  zero")
        else:
            print("Positive number")
        break
    else:
        print("Invalid Input")
        print("Try again")
#now it's working we can handle error using nested statement without try/except statement



