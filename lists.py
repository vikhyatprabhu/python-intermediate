# Initialize lists
# Allows duplicates

mylist = ["Mangalore" , "Udupi" , "Bhatkal"]
print(mylist)

#Init empty list
mylist2=list()
print(mylist2)

# Allows different types
list3 =  [ 5 , True , "Sample"]
print(list3)

#Access with index
print(list3[1])
print(list3[-1])

#ITeration

for i in list3:
    print(i)

if "Udupi" in mylist:
    print("Udupi present")

#Methods
print(len(mylist))
#Append
mylist.append("Shirali")
print(mylist)

#Insert
mylist.insert(2  , "Kundapur")
print(mylist)

#Remove last element
item = mylist.pop()
print(mylist)

#Remove specific
mylist.remove("Kundapur")

#Remove all 
mylist2.clear()

# Reverse
mylist.reverse()
print(mylist)

#Copy list
mylistcopy= mylist.copy()
mylistcopy2 = mylist[:]
mylistcopy3 = list(mylist)

mylist.sort()
print(mylist)
print(sorted(mylistcopy))

# Tricks
nameList = ["Vikhyat"] * 5
print(nameList)

dummylist = nameList + mylist
print(dummylist)

#Sublist
print(dummylist[1:4])

# Step index
print(dummylist[::-1]) #Reverses , 3rd number is the step

# List comprehension
numbers = [1 ,2 , 3 , 4 , 5]
squares = [ x*x for x in numbers]
print(squares)

print(squares.index(25))


