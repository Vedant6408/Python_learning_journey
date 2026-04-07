#indexing = accessing element of a squence  using [] (indexing operator)

string1 = "Hybrid Paddy Seed"
sliced_str = string1[1:5] #this code will gonna print (ybri) because of indexing from 1:5
#we expect that this code will print ybrid but it will print ybri because in python it will always print 1:4th character
#it will exclude 5th index
print(sliced_str)