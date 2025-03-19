import random
import hangman_words
stages = ['''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
   =======
''', '''
    +---+
    |   |
    0   |
   /|\  |
     \  |
        |
   =======
''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
   =======
''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
   =======
''', '''
    +---+
    |   |
    0   |
    |   |
        |
        |
   =======
''', '''
    +---+
    |   |
    0   |
        |
        |
        |
   =======
''', '''
    +---+
    |   |
        |
        |
        |
        |
   =======
''']


lives = 6
chosen_word = random.choice(hangman_words.word_list)



placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += " _ "
print(placeholder)

game_over = False
correct_letters = []


while not game_over:
    print(f'************************* {lives} LIVES LEFT   *************************')
    guess = input('Type a letter of the alphabet').lower()

    if guess in correct_letters:
        print(f'***************** You have already guest {guess} *****************')

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            print(f'Cool! "{guess}" is in the word! You got it right!!! ✅')
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "

    print(display)

# TO-DO 2
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed "{guess}", that\'s not in the word. You lose a life ❌')
        if lives == 0:
            game_over = True


    if "_" not in  display:
        game_over = True
        print('************** YOU WIN 🏆 **************')

    if lives == 0:
        print(f'************** YOU LOSE 💀. The secret word was: "{chosen_word}" **************')

# TO-DO 3
    print(stages[lives])
