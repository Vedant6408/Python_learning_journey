#find the largest of two number
inp1 = int(input("enter first number:: "))
inp2 = int(input("Enter second number:: "))
large_num = max(inp1, inp2)
if inp1 == inp2:
    print("both are equal")
else:
    print(f"The largest number is: {large_num}")