#1. username must be 12 character but not more than 12 char.
#2. username must not contain spaces
#3. username must not contain digits

user_input = input("Enter your username: ")
if len(user_input) > 12:
    print("Your username can't be more than 12 character.")
elif not user_input.find(" ") == -1:
    print("Your username can't contain any spaces.")
elif not user_input.isalpha():
    print("Your username can't contain any digits or symbol.")
else:
    print(f"Welcome! {user_input}")