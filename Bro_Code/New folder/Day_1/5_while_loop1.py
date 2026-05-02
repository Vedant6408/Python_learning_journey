# this is gonna be the first tutorials about while loop programs
name = input("Enter your name: ")
while name == "":
    print("you didn't enter your name")
    name = input("Enter your name: ")
print(f"Hey! {name}")

age = int(input('Enter your age: '))
while age < 0:
    print("Invalid input")
    age  = int(input("Enter your age: "))
if age > 100:
        print(f"a human being can't surive for 100 years normally. and you said you're {age} years old that's crazy man")
else:
     print(f"Your are {age} years old.")


food = input("Enter food your like to eat(q for quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like to eat (q for quit): ")
    
print("bye")

num = int(input("Enter a num. between 1 - 100: "))
while num < 0 or num > 100:
    print("not valid, Try AGain !")
    num = int(input("Enter a num. between 1 - 100: "))
print(f"You entered {num}")