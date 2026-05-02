# groceries = [ 
#     ["Sprite","Thums-Up","Coca-cola","Pepsi","Mazza"],
#     ["Realme","Samsung","Xioami","Apple","Asus"]
# ]
# # print(groceries)
# for a in groceries:
#     for j in a:
#         print(j, end=" ")
#     print()

num_pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ("*",0,"#")
)
for numbers in num_pad:
    for keys in numbers:
        print(keys, end=" ")
    print()