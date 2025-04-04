# Alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
txt = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text'
#         forwards by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift a letter forwards by 9? Can you fix the code?

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f'Here\'s the encoded result {cipher_text}')


# TODO-3: Call the 'encrypt()' function and pass in the user inputs.
#         You should see the encrypted message.

encrypt('hello', 2)