#vowel consonant checking program
usr_inp = input("Enter alphabet: ")
while True:
    if len(usr_inp)==1:
        if usr_inp in "aeiou":
            print("It's a vowel")
        else:
            print("It's a consonant")
        break
    else:
        print("Please enter only one character")
        usr_inp = input("Enter alphabet: ")
