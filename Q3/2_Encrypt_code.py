# the code to encrypt

with open('original_code.txt', 'r') as file: # I copy the original code to txt file to test this
    # Read the contents of the file
    original_code = file.read()

def encrypt(text, key):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

key = 13
encrypted_code = encrypt(original_code, key)
print(encrypted_code)