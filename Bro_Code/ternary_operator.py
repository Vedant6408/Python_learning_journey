#ternary operator is just used to make conditional statement in one line
#it is one line shortcut for if-else programs



#Checking number wether positive or negative
# num = 5
# print("Positive" if 0 < num else "negative")


#checking wether the number is odd or even using ternary operator
# num2 = 4
# print("Even" if int(num2/2) == 0 else "Odd")  #after diving by 2 it give floating number i.e 2.0 != 0 that it gives odd
# #but if we convert that number into integer it is possible to expect the right output
# #i just figure out i'm comparing quotient to zero that'w why it is giving odd as a output
# print("Even" if num2 % 2 == 0 else "Odd")


#checking which number is max. & min.
a = 44
b = 78
max_num = a if a > b else b
min_num = a if a < b else b

print(f"max num is: {max_num} & min num is: {min_num}")

age = 10
temperature = 20
status = "Adult" if age>=18 else "Kid"
print(status)
weather = "Hot" if temperature>=32 else "cold"
print(weather)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)