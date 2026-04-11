
# Arithmetic Operators

print(10 + 5)  # simple addition            output: 15
print(10 - 5)  # simple subtraction         output: 5
print(10 * 5)  # simple multiplication      output: 50
print(10 / 5)  # simple division            output: 2.0
print(10 % 3)  # modulus operator           output: 1
print(10 // 3) # floor division             output: 3
print(10 ** 2) # exponentiation             output: 100

sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2

print(sum1)    # output: 150
print(sum2)    # output: 400
print(sum3)    # output: 800


# Assignment Operators

x = 5     # x = 5
print(x)  # output: 5

x += 3    # x = x + 3
print(x)  # output: 8

x = 5
x -= 3    # x = x - 3
print(x)  # output: 2

x = 5
x *= 3    # x = x * 3
print(x)  # output: 15

x = 5
x /= 3    # x = x / 3
print(x)  # output: 1.6666666666666667

x = 5
x %= 3    # x = x % 3
print(x)  # output: 2

x = 5
x //= 3   # x = x // 3
print(x)  # output: 1

x = 5
x **= 3   # x = x ** 3
print(x)  # output: 125

x &= 3    # x = x & 3
print(x)  # output: 1

x |= 3    # x = x | 3
print(x)  # output: 3

x ^= 3    # x = x ^ 3
print(x)  # output: 0

x >>= 3   # x = x >> 3
print(x)  # output: 0

x <<= 3   # x = x << 3
print(x)  # output: 0

print(x := 5)    # x = 5
                 # output: 5


# Comparison Operators

x = 5
y = 3
print(x == y)  #    Equal                           output: False
print(x != y)  #    Not equal                       output: True
print(x > y)   #    Greater than                    output: True
print(x < y)   #    Less than                       output: False
print(x >= y)  #    Greater than or equal to        output: True
print(x <= y)  #    Less than or equal to           output: False


# Logical Operators

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10

x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# Membership Operators

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


# Bitwise Operators

'''
Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
8 = 0000000000001000
9 = 0000000000001001
10 = 0000000000001010
'''
print(5 & 3)  # Bitwise AND          output: 1
print(5 | 3)  # Bitwise OR           output: 7
print(5 ^ 3)  # Bitwise XOR          output: 6
print(~5)     # Bitwise NOT          output: -6
print(5 << 1) # Bitwise Left Shift   output: 10
print(5 >> 1) # Bitwise Right Shift  output: 2


# Operator Precedence

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

print(100 + ~3)

"""
Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""

print(100 - 3 ** 3)

"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""

print(6 & 2 + 1)

"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2
"""

print(6 ^ 2 + 1)

"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5
"""

print(8 >> 4 - 2)   # (>>) means divide the number by 2 to the power of n (where n is the number of shifts)

"""
Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 8 >> 2 = 2
"""

print(16 << 8 - 2)   # (<<) means multiply the number by 2 to the power of n (where n is the number of shifts)

"""
Bitwise left shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
The calculation above reads 16 << 6 = 1024
"""

print(6 | 2 + 1)

"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7
"""
print(6 & 2 + 1)    

"""
Bitwise AND has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 & 3 = 2
"""

print(6 ^ 2 + 1)

"""
Bitwise XOR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 ^ 3 = 5
"""







