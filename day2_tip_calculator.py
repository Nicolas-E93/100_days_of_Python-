# Reference the position of the characters in a string
print('Hello'[-2])
print('Hello'[3])

# Data Types
# Strings
print("123" + "456")

# Integer
print(123 + 456)

# Large numbers
print(123_456_789)

# Float = Floating point number
print(3.12345)

# Boolean
print(True)
print(False)

#Len()
print(len("1234"))

# Find out the data type by using type()
print(type('abc'))
print(type(123))
print(type(123.12))
print(type(True))

# Type conversion
print("123" + "456") # This will just concatenate these two strings
print(int("123") + int("456")) # This will turn the string into int and will perform a mathematical operation

# Task
#print("Number of letters in your name: " + len(input("Enter your name")))
#print("Number of letters in your name: " + str(len(input("Enter your name")))) # Solution
print("My age" + str(12))

# Math operators
print(5 + 5)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(2 ** 3) #2 to the power of 3 = 8

#PEMDAS when we have more than one mathematical operation in the same line
#parentheses, exponents, multiplication/division, addition/subtraction
# ()
# **
# * OR /
# + OR -
print(3 * 3 + 3 / 3 - 3)

# coding challenge
height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height ** 2

print(int(bmi)) # not an ideal solution here, we want to round the number
print(round(bmi))
print(round(bmi, 2))

# when manipulating values we can use:
score = 0

# user scores a point
score = score + 1 # long version
score += 1 # much more practical version
print(score)

# f-strings
print("Your score is " + str(score)) # This is painful to do sometimes
print(f"Your score is {score}")

# <!-------Tip Calculator-------->
print("Welcome to the tip calculator!")
total_bill = float(input("What's the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?"))
num_people = int(input(f"How many people to split the bill?"))

result = (total_bill * tip_percentage / 100 + total_bill) / num_people
print(f"Each person should pay: ${round(result,2)}")
