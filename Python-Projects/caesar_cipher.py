import string 
alphabet=string.ascii_lowercase
word=input("please type word: ").lower()
encrypted_word=""

for letter in word:
    original_position = alphabet.index(letter)
    new_position = (original_position + 2)%26
    encrypted_word += alphabet[new_position]
print(f"Here is the encrypted word: {encrypted_word}")
