def separate_and_convert(s):
    # Separate the string into numbers and letters

    number_string = "".join([char for char in s if char.isdigit()])
    letter_string = "".join([char for char in s if char.isalpha()])

    # Convert even numbers to their ASCII code decimal values

    even_numbers_ascii = [ord(char) for char in number_string if int(char) % 2 == 0]
    uppercase_letters_ascii = [ord(char) for char in letter_string if char.isupper()]

    return number_string, letter_string, even_numbers_ascii, uppercase_letters_ascii


# Example usage

s = "S6aAww1984sktr235270ayYmn145ss785fsq31D0"
number_string, letter_string, even_numbers_ascii, uppercase_letters_ascii = (
    separate_and_convert(s)
)

print("Number string:", number_string)
print("Letter string:", letter_string)
print("Even numbers ASCII:", even_numbers_ascii)
print("Uppercase letters ASCII:", uppercase_letters_ascii)


def decrypt_cryptogram(ciphered_quote, shift_key):
    decrypted_quote = ""
    for char in ciphered_quote:
        if char.isalpha():
            shift = shift_key % 26
            if char.isupper():
                # Decrypt uppercase letters

                decrypted_quote += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                # Decrypt lowercase letters

                decrypted_quote += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged

            decrypted_quote += char
    return decrypted_quote


def brute_force_decrypt(ciphered_quote):
    for shift_key in range(1, 26):
        decrypted_quote = decrypt_cryptogram(ciphered_quote, shift_key)
        print(f"Shift Key {shift_key}: {decrypted_quote} \n")


# Example usage

ciphered_quote = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
brute_force_decrypt(ciphered_quote)
# Based on the output, the shift key that gives the original quote is 13.