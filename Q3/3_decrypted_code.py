with open('encrypted_text.txt', 'r') as file:
    # Read the contents of the file
    encrypted_code = file.read()

def decrypt(encrypted_text, key):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
    
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = 13

decrypted_code = decrypt(encrypted_code, key)
print("Decrypted: ", decrypted_code)