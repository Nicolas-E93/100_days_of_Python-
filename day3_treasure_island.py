'''# IF STATEMENTS
print("Welcome to the rollercoaster")
height = int(input("What is your height?"))

if height > 180:
    print("You can ride the rollercoaster")
    age = int(input("What's your age?"))
    bill = 0
    if age <= 8:
        bill = 5
        print(" child ticket is $5.")
    elif age <=18:
        bill = 7
        print("teenage ticket is $7.")
    elif age > 18:
        bill = 12
        print("adult ticket is $12.")
    want_photo = input("Do you want a photo? If so type 'yes'")
    if want_photo == "yes":
        bill += 3
        print(f"The total price of your ticket is ${bill}")
else:
    print("Sorry! You need to grow taller to ride the roller caster")

# Challenge
number = int(input("Type a number, please\n"))
result = number % 2

if result == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# CODING CHALLENGE ✅
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")'''

# Coding Challenge - Python Pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")

bill = 0

if size == "S":
    bill = 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3
else:
    print("❌Select a valid pizza size, please")
    exit()
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"\n🛒 Your order summary:\n- Pizza size: {size}\n- Pepperoni: {pepperoni}\n- Extra cheese: {extra_cheese}\n💵 Total: ${bill}")
