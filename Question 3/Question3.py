# Question 3 Task 1

# Key generation method (Given in Question)
def keygen() -> int:
    # fixing this code will reveal the key:

    total = 0
    for i in range(5):
        for j in range(3):
            if (
                i + j == 5
            ):  # among 15 different combinations of (i, j) only (3, 2) and (4, 1) will satisfy this condition
                total += i + j  # total += 5 when the condition is met
            else:  # all other combinations of (i, j)
                total -= (
                    i - j
                )  # might lead to a negative value for example with combinations (0, 1) (0, 2) (1, 2)
    # total will always remain at -1

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    # Total will always remain at 13 to my understanding, so i guess the key will be 13

    return total

# --------------------------------

# Question 3 Task 2 (Encryption and Decryption)

# Encryption method using a Caesar cipher (Given in Question)
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check for alphabetic character
            shifted = ord(char) + key  # Shift character by the key value
            
            # Handle lowercase letters
            if char.islower():
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
            
            # Handle uppercase letters
            elif char.isupper():
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
            encrypted_text += chr(shifted)  # Add the encrypted character to result
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text


# Decryption method (created by reversing given encryption function)
def decrypt(encrypted_text, key):
    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha():  # Check for alphabetic character
            shifted = ord(char) - key  # Reverse the shift by subtracting the key
            # Handle wrap-around for lowercase letters

            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
                elif shifted > ord("z"):
                    shifted -= 26
            # Handle wrap-around for uppercase letters

            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
                elif shifted > ord("Z"):
                    shifted -= 26
            decrypted_text += chr(shifted)  # Add the decrypted character to result
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text


# Read encrypted text provided in the image
with open("Question 3/encrypted_text.txt", "r") as file:
    encrypted_code = file.read()

# Decrypt the provided text with the key
key = keygen()  # Generate key

decrypted_code = decrypt(
    encrypted_code, key
)  # call decrypt function passing encrypted text and generated key
print("Decrypted: ", decrypted_code)  # print decrypted code for debugging

# save decrypted code as original_code.py
with open("Question 3/original_code.py", "w") as file:
    file.write(decrypted_code)
