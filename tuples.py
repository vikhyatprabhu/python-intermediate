#Tuple : ordered , immutable , allows duplicate
mytuple = ("Vikhyat" , 28 , "Shirali")
print(mytuple)

singletuple = ("Vikhyat",)
print(singletuple)

#Tuple from iterable
mytuple = tuple(["Vikhyat" , 28 , "Shirali"])
print(mytuple)

item = mytuple[0]
print(item)

# NOT SUPPORTED assignment 
# mytuple[1] = 29

#Loop
for x in mytuple:
    print(x)

letters = ('a' , 'b' , 'b' , 'c' , 'a', 'e', 'e')
print(letters.count('b'))
print(letters.index('e'))

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000))
