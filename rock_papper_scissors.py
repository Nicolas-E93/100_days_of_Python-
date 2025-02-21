import random

# random integers:
'''random_int = random.randint(1, 10)
print(random_int)'''

# random floating points
'''random_number_0_to_1 = random.random()* 10
print(random_number_0_to_1)'''

# second option to do random floating points
'''random_float = random.uniform(1, 10)
print(random_float)'''

# Coding challenge
random_number = random.randint(1, 2)

if random_number == 1:
    print("Heads")
else:
    print("Tails")

'''# Data Types: LISTS
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "connecticut"]
# updating the items in the list:
states_of_america[1] = "pencilvania"
print(states_of_america[1])
# adding one item to the end of a list:
states_of_america.append("Angelaland")
# adding items to the end of a list:
states_of_america.extend(["New State one", "New State two"])

# Coding challenge
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# 1 Option
random_person = random.randint(0,4)
print(friends[random_person])
# 2 Option
print(random.choice(friends))

#printing len to know how many items we have in a list
print(len(states_of_america))

# Nested lists:
# dirty_dozen = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "spinach", "kale", "tomatoes", "potatoes"]
fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries"]
vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]
# Creating a nested list:
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][3]) # Output: "celery". First index clarifies which list. Second index clarifies which item.'''

# Coding Challenge: Rock, Scissors, Papers
elements = ["🪨", "📄", "✂️"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if user_choice >= 0 and user_choice <=2:
    print(elements[user_choice])
print("computer chose:")
ai_choice = random.randint(0,2)
print(elements[ai_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. You lose 💀💀💀")
elif user_choice == 0 and ai_choice == 0:
    print("Draw ⚔️")
elif user_choice == 0 and ai_choice == 1:
    print("You lose 💀")
elif user_choice == 0 and ai_choice == 2:
    print("You win 🏆")
elif user_choice == 1 and ai_choice == 0:
    print("You win 🏆")
elif user_choice == 1 and ai_choice == 1:
    print("Draw ⚔️")
elif user_choice == 1 and ai_choice == 2:
    print("You lose 💀")
elif user_choice == 2 and ai_choice == 0:
    print("You lose 💀")
elif user_choice == 2 and ai_choice == 1:
    print("You win 🏆")
elif user_choice == 2 and ai_choice == 2:
    print("Draw ⚔️")

