#uppercase lowercase checking program
usr_inp1 = input("Enter whatever you want to type::  ")
if usr_inp1.isalpha():
    if usr_inp1.isupper():
        print("You entered uppercase alphabet") 
    elif usr_inp1.islower():
        print("You entered lowercase alphabet")
    else:
        print('You entered mixed up of uppercase & lowercase')
else:
    print("Invalid input")
    print('try typing only alphabet')