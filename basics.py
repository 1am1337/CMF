from collections import Counter

my_list = [0,3,-2,1]
print(my_list)
sortedList = sorted(my_list) #reverse = True 
print(sortedList)

myListSquared = [i**2 for i in my_list]
print(myListSquared)

myList2 = ["1", "3", "3", "7"]
print(Counter(myList2))
print(myList2.count("3"))
myList2Counted = Counter(myList2)
print(myList2Counted["3"])
print(list(myList2Counted.items()))


myString = "abc"
myString2 = "ABC"
print(myString == myString2)
print(myString.lower() == myString2.lower())