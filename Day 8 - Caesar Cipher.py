from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def encrypt(message, shift):
    new_message = message
    for index in range(len(message)):
        letter_index = alphabet.index(message[index])
        new_index = letter_index + int(shift)
        if new_index > len(alphabet):
            new_index -= len(alphabet)
        new_message[index] == alphabet[new_index]
    return new_message

encode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
message = input("Type your message: \n")
shift = input("Type the shift number: \n")

if encode == 'encode':
    new_message = encrypt(message, shift)
    print(f"Your new message is: {new_message}")
#elif encode == 'decode':
