import random

word_list = ['house', 'book', 'computer']
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input('Type a letter of the alphabet').lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')

# I learnt that for letter - letter is a variable for each of the letter in the
# chosen word, then we compare them against "guess"

#for letter in chosen_word:
#    if guess in chosen_word:
#        print('Right')
#    if guess not in chosen_word:
#        print('Wrong')'''

# TO-DO 1.1

placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_ "

print(placeholder)

# TO-DO 1.2

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += " _ "

print(display)

