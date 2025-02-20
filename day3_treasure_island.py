# IF STATEMENTS
print("Welcome to the rollercoaster") # Roller Coaster Challenge
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
    midlife_crisis = input("Do you have a midlife_crisis? yes or no")
    if midlife_crisis == "yes" and age > 44 and age < 56:
        print("Everything is going to be okay. Ride for free with us!")

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
    print("overweight")

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

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("❌Select a valid pizza size, please")
    exit()

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"\n🛒 Your order summary:\n- Pizza size: {size}\n- Pepperoni: {pepperoni}\n- Extra cheese: {extra_cheese}\n💵 Total: ${bill}")

# Final Coding Challenge 'The Treasure Island'
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
user_choice1 = input("You're on dangerous island. Where do you want to go? left or right?\n")

if user_choice1 == "left" or user_choice1 == "Left":
    user_choice2 = input("You've landed to the shore. Would you like to do? swim to the other "
                         "island or wait for a boat?\n")
    if user_choice2 == "wait for a boat" or user_choice2 == "Wait for a boat":
        user_choice3 = input("You've arrived to a place where there are three doors, which door "
                             "do you want to walk into? Yellow, Red, or Blue?")
        if user_choice3 == "Yellow" or user_choice3 == "yellow":
            print("Congratulations. You've found the treasure!🏆")
        else:
            print("You've gotten attacked by tigers. Game over")
    else:
        print("You got attacked by crocodiles. Game over")
else:
    print("Fall into a hole. Game Over.")
