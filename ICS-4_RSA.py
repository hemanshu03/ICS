import random

def prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

def gcd(p, q):
    while q:
        p , q = q , p%q
    return p

def random_p():
    print("\nSelecting 2 random prime numbers between 0 and 999..")
    p = 4
    q = 4
    while not prime(p):
        p = random.randint(0, 999)
    
    while not prime(q):
        q = random.randint(0, 999)
    
    return p, q

def key():
    p , q = random_p()
    
    n = p * q

    phi = (p - 1) * (q - 1)

    print(f"\nSelected prime numbers are: {p} and {q}.\nCalculated n [n = p × q] = {n}\nCalculated Φ(n) [Φ(n) = (p-1) × (q-1)] = {phi}")

    print(f'\nChoosing e such that GCD(e, Φ({phi})) comes out to be 1...')

    for e in range(2, phi):
        if gcd(e, phi) == 1:
            print(f'\nFound e such that the GCD( {e}, {phi} ) = 1. e came out to be {e}')
            break

    for k in range(0, 100000):
        d = (1 + (k*phi)) / e
        if d == int(d):
            d = int(d)
            print(f'k = {k}\nd = {d}')
            break
        
    print(f'\nUsing numbers {p} and {q}, Public key is ({e}, {n}) and Private key is ({d}, {n})\n')
    
    return e, n, d

def mod(m, e, n):
    result = 1
    m = m % n
    while e > 0:
        if e % 2 == 1:
            result = (result * m) % n
        e = e // 2
        m = (m * m) % n
    return result

def string_to_ascii(message):
    return [ord(char) for char in message]

def ascii_to_string(ascii_list):
    return ''.join([chr(ascii_val) for ascii_val in ascii_list])

message = input("Enter a message to encrypt: ")
ascii_message = string_to_ascii(message)

e, n, d = key()

print(f'e is {e} and n is {n}')

ciphertext = [mod(m, e, n) for m in ascii_message]
deciphertext = [mod(c, d, n) for c in ciphertext]

encrypted_message = ascii_to_string(ciphertext)
decrypted_message = ascii_to_string(deciphertext)

print(f'Encrypted message: {encrypted_message}')
print(f'Decrypted message: {decrypted_message}')
