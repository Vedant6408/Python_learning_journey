#this is gonna be the first tutorials about while loop programs
# name = input("Enter your name: ")
# while name == "":
#     print("you didn't enter your name")
#     name = input("Enter your name: ")
# print(f"Hey! {name}")

age = int(input('Enter your age: '))
while age < 0:
    print("Age can't be in negative")
    age  = int(input("Enter your age: "))
if age > 100:
        print(f"a human being can't surive for 100 years normally. and you said you're {age} years old that's crazy man")
else:
     print(f"Your are {age} years old.")