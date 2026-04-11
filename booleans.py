a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# Output: b is not greater than a

# Most Values are True

bool("abc")
print(bool("abc"))

bool(123)
print(bool(123))

bool(["apple", "cherry", "banana"])
print(bool(["apple", "cherry", "banana"]))




# Some Values are False

bool(False)
print(bool(False))
bool(None)
print(bool(None))
bool(0)
print(bool(0))
bool("")
print(bool(""))
bool(())
print(bool(()))
bool([])
print(bool([]))
bool({})
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

# Print "YES!" if the function returns True, otherwise print "NO!"

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")