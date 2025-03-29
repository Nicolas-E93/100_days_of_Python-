
# Functions that allow for inputs
def greet(name_of_user):
    print(f'Hello {name_of_user}, we are excited to have you here')

name = input('What is your name?\n')

greet(name)

# Function to determine how many weeks someone has assuming they'll live 90 years
def life_in_weeks(age):
    result = 4680 - (age * 52)
    print(f'You have {result} weeks left.')

current_age = int(input('How old are you?\n'))

life_in_weeks(current_age)

