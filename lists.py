thislist = ["apple", "banana", "cherry"] 
print(thislist[1]) 

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:       # To check if an item exists in the list, use the in keyword.
  print("Yes, 'apple' is in the fruits list")
  
  
# Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"  # To change the value of a specific item, refer to the index number.
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  # The number of items in the replacement list is the same as the number of items being replaced.
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]  # The number of items in the replacement list is different from the number of items being replaced.
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]  # The number of items in the replacement list is different from the number of items being replaced.
print(thislist)


# Insert Items

thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")  # The insert() method inserts an item at the specified index.

print(thislist) 


# Add List Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")  # The append() method adds an item to the end of the list.
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # The insert() method inserts an item at the specified index.
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # The extend() method adds the specified list elements (or any iterable) to the end of the current list.
print(thislist)


# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # The extend() method adds the specified list elements (or any iterable) to the end of the current list.
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)  # The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
print(thislist)


# Remove List Items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # The remove() method removes the specified item.
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") 
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # The pop() method removes the specified index, 
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # If you do not specify the index, the pop() method removes the last item.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]  # The del keyword also removes the specified index, but you can also delete the list completely.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist # Delete the entire list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # The clear() method empties the list.
print(thislist)


# Loop Lists

thislist = ["apple", "banana", "cherry"]
for x in thislist: # dispalys the list one by one.
    print(x)

thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):  # The len() function returns the number of items in the list.
  print(thislist[i])
  
# While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):  # The len() function returns the number of items in the list.
  print(thislist[i])
  i = i + 1
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  # A short hand for loop that will print all items in one line.


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]  # A short hand for loop that will print all items in one line.  








