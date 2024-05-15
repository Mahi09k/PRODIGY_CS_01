# Encryption Algorithm
def encrypt(text, s):
    result = ""
    # Traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        # If it's not a letter, leave it as is
        else:
            result += char
    return result

# Decryption Algorithm
def decrypt(text, s):
    result = ""
    # Traverse text
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        # If it's not a letter, leave it as is
        else:
            result += char
    return result

# Main function with menu
def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter your Message to Encrypt: ")
            s = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, s)
            print("Text : " + text)
            print("Shift Value : " + str(s))
            print("The Encrypted text is : " + encrypted_text)

        elif choice == '2':
            text = input("Enter your Message to Decrypt: ")
            s = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, s)
            print("Text : " + text)
            print("Shift Value : " + str(s))
            print("The Decrypted text is : " + decrypted_text)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
