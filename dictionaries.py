thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,  # This will be overwriten by the next "year" value
  "year": 2020,
  "color": ["red", "white", "blue"]
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Access Items--------------------------> 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# Check if Key Exists-------------------------->

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

if "model" not in thisdict:
    print("No, 'model' is not one of the keys in the thisdict dictionary")



# Remove items-------------------------->

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()  # The popitem() method removes the last inserted item. In this case, It is the "Year".
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# Loops-------------------------->

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #prints the keys
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x]) # prints the values 



