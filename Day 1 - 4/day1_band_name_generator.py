# Task 1
# Print statement in different line (this uses only one print statement)
print('Hello world!\nHello world!\nHello world!')

# Task 2
# Concatenating strings
print("Hello" + " " + "Angela")
print("Hello " + "Angela")
print("Hello" + " Angela")

# Task 3
# input function
print("Hello "+ input("What is your name?") + "!")

# Task 4
# Variables and len() function
print(len(input("What is your name?")))
# Breaking down the 1-line code above
username = input("What is your name?")
length = len(username)
print(length)

# Final project: Band name generator
print("Welcome to the brand-new band name generator")
city = input("What's the name of the city you grew up in?\n")
pet_name = input("What's the name of your pet?\n")
print("Your band name could be: " + city + " " + pet_name)
