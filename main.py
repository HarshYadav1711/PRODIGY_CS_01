letters = "gusfdhuibsuauiuiuiabuiai"
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'decrypt':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result

print()
print("CAESAR CIPHER PROGRAM")
print()

print("Encrypt or Decrypt?: ")
user_input = input("encrypt/decrypt: ").lower()
print()

if user_input == "encrypt":
    print("Encrypt option selected")
    print()
    key = int(input("Enter the key: "))
    text = input("Enter the text to be encrypted: ")
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f"Cipher Text: {ciphertext}")

elif user_input == "decrypt":
    print("Decrypt option selected")
    print()
    key = int(input("Enter the key: "))
    text = input("Enter the text to be decrypted: ")
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f"Plain Text: {plaintext}")