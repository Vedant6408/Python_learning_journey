# list1 = [1, 2 , 2, 3, 5] #so we can't use end function like loop statement
# print(list1, end="-")

# for y in range(4):
#     for o in range(1,11):
#         print(o,end=f"")
#     print(end=" ")

# rows = int(input("Enter a # of rows: "))
# column = int(input('Enter a # of column: '))
# symbol = input("Which type of symbol u wanna use: ")
# for y in range(rows):
#     for x in range(column):
#         print(symbol, end=" ")
#     print()
row = 10
for i in range(1, row + 1):
    for j in range(i):
        print("*",end=" ")
    print()