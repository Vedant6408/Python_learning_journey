#format specifier ----> format value based on what flag are inserted
#       formula-->{value:flags}

value1 = 13.403
value2 = 14.75
value3 = 7.24578
#(:._f) in the black space we will fill any number according to how much digits we want to print after decimal
print(f"Value1 is: ${value1:.2f}")
print(f"Value2 is: ${value2:.1f}")
print(f"Value3 is: ${value3:.3f}")
print("_________________________________________")
#(:<) means left justify
print("Left Justified value printed")
print(f"Value1 is: ${value1:<14}")
print(f"Value2 is: ${value2:<14}")
print(f"Value3 is: ${value3:<14}")
#(:>) means right justify
print("_______________________________")
print("Righ Justified Value Printed")
print(f"Value1 is: ${value1:>14}")
print(f"Value2 is: ${value2:>14}")
print(f"Value3 is: ${value3:>14}")
#(:14) means justify the value to 14 character, it works like right justify
print("___________________________________")
print(f"Value1 is: ${value1:14}")
print(f"Value2 is: ${value2:14}")
print(f"Value3 is: ${value3:14}")
print("_____________________________")
#(:014) means add zero in all value from zero index
print("zero printed from 0 index ")
print(f"value1 is: ${value1:014}")
print(f"value2 is: ${value2:014}")
print(f"value2 is: ${value2:014}")
#(:^) centerlined all the value
print("_________________________")
print("centerlined value")
print(f"value1 is: ${value1:^14}")
print(f"value2 is: ${value2:^14}")
print(f"value2 is: ${value2:^14}")


print("________________________")
#(:,) thousand place will seperated with commas
value4 = 245324.933434
print(f"The commas seperated value is: {value4:,}")
print(f"The final format is: {value4:+,.2f}") #it means it will seperate thousand in commas and print 3 digits after decimal
#and that + sign it will show the sign (+/-)
#in formulas {value4:+,.Nf}, N belongs to  natural number
