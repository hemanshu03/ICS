def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to uppercase for easier manipulation
            char = char.upper()
            
            # Calculate the new character position
            char_code = ord(char) - ord('A')
            new_char_code = (char_code + shift) % 26
            
            # Convert back to the original case
            new_char = chr(new_char_code + ord('A'))
            
            # Restore the original case
            if not is_upper:
                new_char = new_char.lower()
            
            result += new_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char
    
    return result

def caesar_decipher(cipher_text, shift):
    result = ""
    
    for char in cipher_text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to uppercase for easier manipulation
            char = char.upper()
            
            # Calculate the new character position
            char_code = ord(char) - ord('A')
            new_char_code = (char_code - shift) % 26
            
            # Convert back to the original case
            new_char = chr(new_char_code + ord('A'))
            
            # Restore the original case
            if not is_upper:
                new_char = new_char.lower()
            
            result += new_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char
    
    return result


# Example usage:
text = input("Enter text to input: ")
shift = int(input("Enter number of shifts: "))
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)



