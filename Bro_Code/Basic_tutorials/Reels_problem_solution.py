# name = "python"
# if name == "java" or "html":
#     print("Login valid")
# else:
#     print("invalid login")


#printing 1 to 10 using while loop
# a = 1
# while True:
#     if a <= 10:
#         print(a)
#         a += 1
#     else:
#         break
    

#palidrome number checking program
# usr_input = input("Enter your number:: ")
# if usr_input[::-1]==usr_input:
#     print("your number is palidrome")
# else:
#     print("your number isn't palidrome number")

# usr_input2 = int(input('enter'))
# something = usr_input2 % 60
# print(something)

cars = ["Porsche", "BMW", "Audi"]
trending = []
for c in cars:
    if c == "BMW" or "Porsche":
        trending.append(c)
print(trending)