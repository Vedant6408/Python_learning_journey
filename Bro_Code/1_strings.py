name = input("Enter your name: ")
# length = len(name)
# length = name.find("o") #it always find the find occurence
# length = name.rfind("e") #this is the method to find the last occurence
#if python don't find the occurence of any letter it will return -1
length = name.find("x")
#we can captalize the first letter of string using captalize() function
length = name.capitalize()
#upper() function make all letter uppercase
length = name.upper()
#lower() function make all letter lowercase
length = name.lower()
#isdigit() if my string contains all  digits then it will return true otherwise false
length = name.isdigit()
#isaplha() if my string contains all aphabets then it will return true othersie false
length = name.isalpha()
#count() it is used to count how many character in the ceratin variable(string, integer,float)
length = name.count()
#replace() it is used to replace the targated character in the string
print(length)

print(str(help))