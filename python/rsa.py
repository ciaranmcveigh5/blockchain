#!/usr/bin/env python

# This example demonstrates RSA public-key cryptography in an
# easy-to-follow manner. It works on integers alone, and uses much smaller numbers
# for the sake of clarity.

#####################################################################
# First we pick our primes. These will determine our keys.
#####################################################################

# Pick P,Q,and E such that:
#  1: P and Q are prime; picked at random.
#  2: 1 < E < (P-1)*(Q-1) and E is co-prime with (P-1)*(Q-1)

P = 97  # First prime
Q = 83  # Second prime
E = 53  # usually a constant; 0x10001 is common, prime is best


#####################################################################
# Next, some functions we'll need in a moment:
#####################################################################
# Note on what these operators do:
# %  is the modulus (remainder) operator: 10 % 3 is 1
# // is integer (round-down) division: 10 // 3 is 3
# ** is exponent (2**3 is 2 to the 3rd power)

# Brute-force (i.e. try every possibility) primality test.
def isPrime(x):
    if x % 2 == 0 and x > 2: return False  # False for all even numbers
    i = 3  # we don't divide by 1 or 2
    sqrt = x ** .5
    while i < sqrt:
        if x % i == 0: return False
        i += 2
    return True


# Part of find_inverse below
# See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def eea(a, b):
    if b == 0: return (1, 0)
    (q, r) = (a // b, a % b)
    (s, t) = eea(b, r)
    return (t, s - (q * t))


# Find the multiplicative inverse of x (mod y)
# see: http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def find_inverse(x, y):
    inv = eea(x, y)[0]
    if inv < 1: inv += y  # we only want positive values
    return inv


#####################################################################
# Make sure the numbers we picked above are valid.
#####################################################################

if not isPrime(P): raise Exception("P (%i) is not prime" % (P,))
if not isPrime(Q): raise Exception("Q (%i) is not prime" % (Q,))

T = (P - 1) * (Q - 1)  # Euler's totient (intermediate result)
# Assuming E is prime, we just have to check against T
if E < 1 or E > T: raise Exception("E must be > 1 and < T")
if T % E == 0: raise Exception("E is not coprime with T")

#####################################################################
# Now that we've validated our random numbers, we derive our keys.
#####################################################################

# Product of P and Q is our modulus; the part determines as the "key size".
MOD = P * Q

# Private exponent is inverse of public exponent with respect to (mod T)
D = find_inverse(E, T)

# The modulus is always needed, while either E or D is the exponent, depending on
# which key we're using. D is much harder for an adversary to derive, so we call
# that one the "private" key.

print("public key: (MOD: %i, E: %i)" % (MOD, E))
print("private key: (MOD: %i, D: %i)" % (MOD, D))

# Note that P, Q, and T can now be discarded, but they're usually
# kept around so that a more efficient encryption algorithm can be used.
# http://en.wikipedia.org/wiki/RSA#Using_the_Chinese_remainder_algorithm

#####################################################################
# We have our keys, let's do some encryption
#####################################################################

# Here I only focus on whether you're applying the private key or
# applying the public key, since either one will reverse the other.

import sys

print("Enter \">NUMBER\" to apply private key and \"<NUMBER\" to apply public key; \"Q\" to quit.")

while True:
    sys.stdout.write("? ")
    line = sys.stdin.readline().strip()
    if not line: break
    if line == 'q' or line == 'Q': break

    if line[0] == '<':
        key = E
    elif line[0] == '>':
        key = D
    else:
        print("Must start with either < or >")
        print("Enter \">NUMBER\" to apply private key and \"<NUMBER\" to apply public key; \"Q\" to quit.")
        continue

    line = line[1:]
    try:
        before = int(line)
    except ValueError:
        print("not a number: \"%s\"" % (line))
        print("Enter \">NUMBER\" to apply private key and \"<NUMBER\" to apply public key; \"Q\" to quit.")
        continue

    if before >= MOD:
        print("Only values up to %i can be encoded with this key (choose bigger primes next time)" % (MOD,))
        continue

    # Note that the pow() built-in does modulo exponentation. That's handy, since it saves us having to
    # implement that ablity.
    # http://en.wikipedia.org/wiki/Modular_exponentiation

    after = pow(before, key, MOD)  # encrypt/decrypt using this ONE command. Surprisingly simple.

    if key == D:
        print("PRIVATE(%i) >>  %i" % (before, after))
    else:
        print("PUBLIC(%i) >>  %i" % (before, after))



# '''
# 620031587
# Net-Centric Computing Assignment
# Part A - RSA Encryption
# '''
#
# import random
#
# '''
# Euclid's algorithm for determining the greatest common divisor
# Use iteration to make it faster for larger integers
# '''
#
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
#
# '''
# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
# '''
#
#
# def multiplicative_inverse(e, phi):
#     d = 0
#     x1 = 0
#     x2 = 1
#     y1 = 1
#     temp_phi = phi
#
#     while e > 0:
#         temp1 = temp_phi / e
#         temp2 = temp_phi - temp1 * e
#         temp_phi = e
#         e = temp2
#
#         x = x2 - temp1 * x1
#         y = d - temp1 * y1
#
#         x2 = x1
#         x1 = x
#         d = y1
#         y1 = y
#
#     if temp_phi == 1:
#         return d + phi
#
#
# '''
# Tests to see if a number is prime.
# '''
#
#
# def is_prime(num):
#     if num == 2:
#         return True
#     if num < 2 or num % 2 == 0:
#         return False
#     for n in xrange(3, int(num ** 0.5) + 2, 2):
#         if num % n == 0:
#             return False
#     return True
#
#
# def generate_keypair(p, q):
#     if not (is_prime(p) and is_prime(q)):
#         raise ValueError('Both numbers must be prime.')
#     elif p == q:
#         raise ValueError('p and q cannot be equal')
#     # n = pq
#     n = p * q
#
#     # Phi is the totient of n
#     phi = (p - 1) * (q - 1)
#
#     # Choose an integer e such that e and phi(n) are coprime
#     e = random.randrange(1, phi)
#
#     # Use Euclid's Algorithm to verify that e and phi(n) are comprime
#     g = gcd(e, phi)
#     while g != 1:
#         e = random.randrange(1, phi)
#         g = gcd(e, phi)
#
#     # Use Extended Euclid's Algorithm to generate the private key
#     d = multiplicative_inverse(e, phi)
#
#     # Return public and private keypair
#     # Public key is (e, n) and private key is (d, n)
#     return ((e, n), (d, n))
#
#
# def encrypt(pk, plaintext):
#     # Unpack the key into it's components
#     key, n = pk
#     # Convert each letter in the plaintext to numbers based on the character using a^b mod m
#     cipher = [(ord(char) ** key) % n for char in plaintext]
#     # Return the array of bytes
#     return cipher
#
#
# def decrypt(pk, ciphertext):
#     # Unpack the key into its components
#     key, n = pk
#     # Generate the plaintext based on the ciphertext and key using a^b mod m
#     plain = [chr((char ** key) % n) for char in ciphertext]
#     # Return the array of bytes as a string
#     return ''.join(plain)
#
#
# if __name__ == '__main__':
#     '''
#     Detect if the script is being run directly by the user
#     '''
#     print("RSA Encrypter/ Decrypter")
#     p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
#     q = int(raw_input("Enter another prime number (Not one you entered above): "))
#     print("Generating your public/private keypairs now . . .")
#     public, private = generate_keypair(p, q)
#     print("Your public key is ", public, " and your private key is ", private message = raw_input("Enter a message to encrypt with your private key: ")
#     encrypted_msg = encrypt(private, message)
#     print("Your encrypted message is: ")
#     print(''.join(map(lambda x: str(x), encrypted_msg)))
#     print("Decrypting message with public key ", public, " . . .")
#     print("Your message is:")
#     print(decrypt(public, encrypted_msg))