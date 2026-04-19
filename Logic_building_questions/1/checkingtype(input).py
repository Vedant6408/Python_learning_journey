#check if a character is an alphabet, digit or special characters
# usr_input = input("Enter whatever you want to type: ")
# if usr_input.isdigit():
#     print("You entered digits")
# elif usr_input.isalpha():
#     print("You entered alphabets")
# else:
#     print("your entered symbol or combination of characters.")


#2nd try using module
# import string
# usr_inp = input("Enter whatever you wanna type:: ")
# if usr_inp in string.ascii_letters:
#     print("You entered alphabets")
# elif usr_inp in string.punctuation:          #this program is incomplete bcz it will not print right thing
#     print("you entered symbols")             
# elif usr_inp in string.digits:
#     print("You entered digits")
# else:
#     print("You entered combination of symbols,letter and digits")

#3rd try using module 
import string
usr_inp = input("enter whatever you wanna type:: ")
if all(c in string.punctuation for c in usr_inp):
    print("You entered symbolic character.")
elif all(c in string.ascii_letters for c in usr_inp):
    print("You entered alphabet")
elif all(c in string.digits for c in usr_inp):
    print("you entered digits")
else:
    print("you entered combination of symbolic character, letter & digits.")
    