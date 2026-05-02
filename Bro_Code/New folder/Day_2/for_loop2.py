# for x in range(1,11):
#     print(x)
#what if we don't enter any value after commas in range function
# for x in range(6):
    # print(x)
#if there is not value after commas then it will return 0 to that number, but that number will be excluded

while True:
    usr_inp = input("Enter number: ")
    if usr_inp.isdigit():
        usr_inp = int(usr_inp)
        if usr_inp<=10:
            for usr_inp in range(usr_inp,11):
                print(usr_inp)
            break
        else:
            print("your number is greater than 11.")
            continue        
    else:
        print("invalid input")
        print("try again")