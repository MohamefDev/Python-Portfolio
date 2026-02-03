import string

alphabet = string.ascii_lowercase
word = input("Enter the word to encrypt: ").lower()
shift = int(input("Enter the shift number: "))

encrypted_word = ""

for letter in word:
    if letter in alphabet:
        original_position = alphabet.index(letter)
        new_position = (original_position + shift) % 26
        encrypted_word += alphabet[new_position]
    else:
        encrypted_word += letter

print(f"Encrypted word: {encrypted_word}")


