# Functions with more than 1 input
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'what is it like in {location}?')

user_name = input('What is your name?\n')
user_location = input('Where are you based?\n')

greet_with(user_name, user_location)

# Keyword Arguments
# greet_with(location='Colombia', name='Nicolas')