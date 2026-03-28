def caesar_cipher(text: str, shift: int):
    output = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                output += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                output += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else: 
            output += char
    return output




print(caesar_cipher('mjdshfkshf', 4))










