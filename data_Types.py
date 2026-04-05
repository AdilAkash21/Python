"""

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

"""

# Text Type

x = "Hello World"
print(x)

# Numeric Types

x = 5       # int
y = 3.14    # float
z = 1 + 2j # complex

print(x)
print(y)
print(z)

# Sequence Types

x = ["apple", "banana", "cherry"] # list
y = ("apple", "banana", "cherry") # tuple
z = range(6) # range

print(x)
print(y)
print(z)

# Mapping Type

x = {"name": "John", "age": 30} # dict

print(x)

# Set Types

x = {"apple", "banana", "cherry"} # set
y = frozenset({"apple", "banana", "cherry"}) # frozenset
print(x)
print(y)

# Boolean Type

x = True
y = False
print(x)
print(y)

# Binary Types

x = b"Hello" # bytes
y = bytearray(5) # bytearray
z = memoryview(bytes(5)) # memoryview
print(x)
print(y)
print(z)

# None Type

x = None
print(x)




