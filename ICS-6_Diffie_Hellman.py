from sympy import is_primitive_root
import random

def prime(number):
    if number <= 1:
        return False # 1 is composite, not prime
    
    if number <= 3:
        return True # since 2 and 3 are always prime
    
    if number % 2 == 0 or number % 3 == 0: # if the number is divisible by 2 or 3
        return False
    
    i = 5 #Below this, the algorithm checks if the number is divisible or a root of numbers 5 or greater.
    while i * i <= number: # To check if square roots or not
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def mod(b, e, n):
    result = (b ** e) % n #g^XA mod n
    return result

n = int(input("Enter a prime number p: "))

while not prime(n):
    print(f"\nEntered n, {n} not prime.")
    n = int(input("Enter a prime number p: "))

g = int(input(f"Enter a number g such that it is the primitive root of n i.e., {n}: "))

while not is_primitive_root(g, n):
    print(f"\nEntered g, {g} is not a primitive root of entered n, {n}")
    g = int(input(f"Enter a number g such that it is the primitive root of n i.e., {n}: "))

XA = random.randint(1, n)
XB = random.randint(1, n)
#XA = 2
#XB = 3

print(f"Calculating public key YA = {g}^({XA}) mod {n}")
YA = mod(g, XA, n)
print(f"Calculating public key YB = {g}^({XB}) mod {n}")
YB = mod(g, XB, n)

print(f"\nPublic keys:\nFor A, YA = {YA},\nFor B, YB = {YB}")

print(f"Calculating private key Ka = {YB}^({XA}) mod {n}")
KA = mod(YB, XA, n)
print(f"Calculating private key Kb = {YA}^({XB}) mod {n}")
KB = mod(YA, XB, n)

print(f"\nShared private keys:\nFor A, {KA},\nFor B, {KB}")

print("\n----------xEnd of Programx----------\n")