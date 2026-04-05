'''
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
 
'''

age = 36
txt = f"My name is John, I am {age}"
# By placing an f or F before the opening quotation mark, you tell Python to look for curly braces {}.
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

