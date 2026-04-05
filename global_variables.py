x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()  # This will print "Python is awesome" because the variable x is global and can be used inside the function.


x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()

print("Python is " + x)  # This will print "Python is awesome" because the variable x inside the function is local and does not affect the global variable x.

# The global Keyword

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("Python is " + x)  # This will print "Python is fantastic" because the global keyword makes the variable x inside the function refer to the global variable x.


x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("Python is " + x)  # This will print "Python is fantastic" because the global keyword makes the variable x inside the function refer to the global variable x.










