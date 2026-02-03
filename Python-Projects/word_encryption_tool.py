import string

alphabet = string.ascii_lowercase
word = input("Enter the word to encrypt: ").lower()

try:
    shift = int(input("Enter the encryption key (number): "))
except ValueError:
    shift = 2

encrypted_word = ""

for letter in word:
    if letter in alphabet:
        original_position = alphabet.index(letter)
        new_position = (original_position + shift) % 26
        encrypted_word += alphabet[new_position]
    else:
        encrypted_word += letter

print(f"Encrypted word: {encrypted_word}")

