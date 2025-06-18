def simple_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift + 1) % 26 + shift)
        else:
            result += char
    return result

print(simple_cipher("abc XYZ!"))
