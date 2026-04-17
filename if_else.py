"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""


# If------------------>

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
number = 15
if number > 0:
  print("The number is positive")
  
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
  
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
  
  
# Elif------------------>

"""
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")


age = 25

if age < 13:  #
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
  
  
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")  
  


# Else------------------>

"""
The else keyword catches anything which isn't caught by the preceding conditions.

The else statement is executed when the if condition (and any elif conditions) evaluate to False.

"""

a = 200
b = 33
if b > a:
  print("b is greater than a") # False
elif a == b:
  print("a and b are equal") # False  
else:
  print("a is greater than b") # True, So It will print this statement.
  
  
a = 200
b = 33        # Can have an else without the elif.
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
number = 7  # Checking even or odd numbers

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
  
  
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
  
  
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

# Logical Operators------------------>

# AND Operator

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
# OR Operator

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# NOT Operator

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Mutiple Conditions------------------>

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
  

