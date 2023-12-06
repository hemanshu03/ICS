def feistel_cipher(text, key, rounds, encrypt_round, decrypt_round):
    left, right = text[:len(text)//2], text[len(text)//2:]

    for round in range(rounds):
        new_right = xor(left, encrypt_round(right, key))
        left, right = right, new_right

    encrypted_text = right + left  # Swap left and right for the final output
    return encrypted_text

def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def encrypt_round(right, key):  
    return xor(right, key)

def decrypt_round(right, key):
    return xor(right, key)

# Example usage:
plaintext = input("Enter text to encrypt: ")
key = "SecretKey"
rounds = 8

encrypted_text = feistel_cipher(plaintext, key, rounds, encrypt_round, decrypt_round)
print("Encrypted:", encrypted_text)

decrypted_text = feistel_cipher(encrypted_text, key, rounds, decrypt_round, encrypt_round)
print("Decrypted:", decrypted_text)
