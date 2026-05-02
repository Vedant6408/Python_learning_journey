#for loop --> excute a block of code in a fixed number of time 
#range(start,end_excluded,step_to_skip)
# for a in reversed(range(1,6,3)):#it exclude last value
#     print(a)
# print("Happy Birthday !")

# credit_card_num = "1234-5678-9012-3456" #integer aren't iterable
# for x in credit_card_num:
#     print(x)

for x in range(1,21):
    if x == 14:
        continue
    else:
        print(x)
for x in range(1,21):
    if x == 14:
        break
    else:
        print(x)