import pyfiglet

# Create a menu with big text
def main():
    while True:
        print(pyfiglet.figlet_format("CAESAR CIPHER"))
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
            print("Encrypted Text : " + str(encrypted_text))

        elif choice == '2':
            text = input("Enter your Message to Decrypt: ")
            s = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, s)
            print("Text : " + text)
            print("Shift Value : " + str(s))
            print("Decrypted Text : " + str(decrypted_text))


        elif choice == '3':
            print(pyfiglet.figlet_format("Goodbye!"))
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Encryption Algorithm
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

# Decryption Algorithm
def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result

if __name__ == "__main__":
    main()
