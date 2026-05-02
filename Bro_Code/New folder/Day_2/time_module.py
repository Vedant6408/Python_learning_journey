import time

# time.sleep(4)
# print("Times Up !")

usr_time = int(input("Enter the time in second: "))
# for i in reversed(range(0,usr_time)):
for i in range(usr_time,0,-1):
    second = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    # time.sleep(usr_time)
    time.sleep(1) #there is no difference after swaping line 9 to 10 
    print(f"{hours:02}:{minutes:02}:{second:02}")
print("Time's UP!")