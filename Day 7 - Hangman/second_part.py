import random

word_list = ['house', 'book', 'computer']
chosen_word = random.choice(word_list)
print(chosen_word)

game_over = False
correct_letters = []

while not game_over:
    guess = input('Type a letter of the alphabet').lower()

# TO-DO 1.2

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "
    print(display)

    if "_" not in display:
        game_over = True
        print('You win')