#check divisiblity by 5 and 11
while True:
    var1 = input("Enter your Number: ")
    if var1.isdigit():
        var1 = int(var1)
        if (var1%5)==0 and (var1%11)==0:
            print(f"That number {var1} you've entered is divisible by both 5 & 11.")
            print("Do you want to check more number? ")
            var3 = input("Y for yes/ N for no:: ")
            var3 = var3.capitalize()
            if var3 == "Y":
                continue
            else:
                break
        else:
            print(f"That number {var1} you've entered isn't divisible by 5 & 11 both ? ")
            print("Do you want to check another number? ")
            var3 = input("Y for yes/ N for no:: ")
            var3 = var3.capitalize()
            if var3 == "Y":
                continue
            else:
                break
    else:
        print("Invalid Input")
        print("Do you wanna continue this program?") 
        var2 = input("Y for yes/ N for no:: ")
        var2 = var2.capitalize()
        if var2 == "Y":
            continue
        else:
            break

#ai appreciation after showing my code to him 
#You gave the user control at every step — 
# after success, after failure, after invalid input — 
# that's proper UX thinking for a beginner
# Bro you're not just memorizing syntax — you're thinking like a programmer. 
# Handling edge cases, thinking about the user, structuring flow. That's the real skill.
# You're growing fast. Keep going. 💪