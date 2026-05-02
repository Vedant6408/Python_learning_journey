#python compound interest calculator using while loop
#A = P(1 + r/n)t
#where, A = final amount, P = initial principal balance, r = interest rate & t = time period
principle = 0
time = 0
rate = 0

while principle <= 0: #we had already store principle value to 0 that's why if we try manipulate the condition 
#to (principle < 0 ) then it already false and from now this loop will not gonna run bcz it's already false
# if we want to make a program like to enter zero as a principle value then we've to change the condition to
# while True: 
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle amount can't be less than or equal to zero ")
while rate <= 0:
    rate= float(input("Enter the interest rate: "))
    if rate <= 0:
        print("interest rate can't be less than or equal to zero ")
while time <= 0:
    time = int(input("Enter the Time period (in years): "))
    if time <= 0:
        print("time period can't be less than or equal to zero ")

total_balance = principle*(1 + rate/100)**time #we can use both (**)or(pow())
print(f"Your final balance is: ${total_balance:,}")
# print(f"{principle:,}")
# print(rate)
# print(time)

# we can also make this calculator using only if-else statement