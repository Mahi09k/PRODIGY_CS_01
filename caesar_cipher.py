# Encryption Algorithm
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


text = input("Enter your Message to Encrypt: ")
s = int(input("Enter the shift value: "))
print("Text : " + text)
print("Shift Value : " + str(s))
print("The Encrypted text is : " + encrypt(text, s))