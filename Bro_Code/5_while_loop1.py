#this is gonna be the first tutorials about while loop programs
name = input("Enter your name: ")
while name == "":
    print("you didn't enter your name")
    name = input("Enter your name: ")
print(f"Hey! {name}")