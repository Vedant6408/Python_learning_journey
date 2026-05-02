#indexing = accessing element of a squence  using [] (indexing operator)

string1 = "Hybrid Paddy Seed"
sliced_str = string1[1:5] #this code will gonna print (ybri) because of indexing from 1:5
#we expect that this code will print ybrid but it will print ybri because in python it will always print 1:4th character
#it will exclude 5th index
print(sliced_str)
#There are many types to slice the strings
print(string1[1:]) #it will print from 1st index to last index
print(string1[:])#it will print from 0 index to last index
print(string1[:4]) #it will print from 0 index to 3th index and exclude 4th index
#NOTE: in string slicing if we want to print the 4th index, 8th index it will always exclude that last index
#  [start:end:steps]
# we can also print string skiping some character 
print(string1[::4]) #it will print every character after skiping 3 character
#we can also start printing from last index using negative indexing
print(string1[-5:]) #it will print from last index to -4 index 
#in negative indexing it will always start from -1 index not from 0 index


#exercise 1 (print the last 4 digit of a credit card numberr)
credit_card_number = "1483-2847-2838-2879"
last_4_digit = credit_card_number[-4:]
print("Your Last four digits of credit card is: ")
print(f"XXXX-XXXX-XXXX-{last_4_digit}")


#exercise 2 (reverse the whole credit card number which is now in string format)
reversed_str = credit_card_number[::-1] #it will reverse the whole string
print(f"The reverse of your credit card number: {reversed_str}")
