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

# cars = ["Porsche", "BMW", "Audi"]
# trending = []
# for c in cars:
#     if c == "BMW" or "Porsche":
#         trending.append(c)
# print(trending)

# fruits = ["apple", "banana", "mango", "kiwi", "grape"]
# for f in fruits:
#     if "a" in f:
#         fruits.remove(f)
# print(fruits)

# a = [11,22,33,44,55,66]
# for i in a:
#     a.remove(i)
# print(i)

# x = True
# if x == 1:
#     print("stephen hawking")  #here is the twist once the if statement if true i will not read the elif state after thatif x is True:     
#      #but if we use if statement after if statement then what will gonna happen let's see
# if x is True:
#     print('python') #it also print that python string
# elif x:
#     print("the breif history of time")
# else:
#     print("cosmos")
# #if the if statement is true then all the elif is going to be ignored but if there will be 2 or more if statement then they will also gonna be read by the compiler

countries = ["America","Canda","India","Australia","China","Chile","California"]
for c in countries:
    if c.startswith("C"):
        countries.remove(c)
print(countries)