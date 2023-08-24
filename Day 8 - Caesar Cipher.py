from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(message, shift, direction):
    new_message = ''
    for index in range(len(message)):
        letter_index = alphabet.index(message[index])

        # pick direction of shift based on encode or decode
        if direction == 'encode':
            new_index = letter_index + shift
        else:
            new_index = letter_index - shift

        # wrap around if index goes out of bounds of alphabet list
        if new_index > len(alphabet):
            new_index -= len(alphabet)
        if new_index < 0:
            new_index += len(alphabet)

        new_message += alphabet[new_index]
    return new_message

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
message = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


encrypted_message = caesar(message, shift, direction)
print(f"Your new message is: {encrypted_message}")
