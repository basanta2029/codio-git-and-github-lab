import string

def caesar_cipher(message, shift):
    message = message.upper()
    alphabet = string.ascii_uppercase
    encoded_message = ""

    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % 26
            shifted_char = alphabet[shifted_index]
            encoded_message += shifted_char
    return encoded_message
message = input("Write a message: ")
shift =int(input("Number of shift: "))
encoded_message = caesar_cipher(message, shift)
for i in range(0, len(encoded_message), shift):
    print(encoded_message[i:i+shift], end=" ")
    if i % 50 == 45:
        print()
print()