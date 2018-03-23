import hashlib
import binascii
import base58

# publicKey = b'0450863AD64A87AE8A2FE83C1AF1A8403CB53F53E486D8511DAD8A04887E5B23522CD470243453A299FA9E77237716103ABC11A1DF38855ED6F2EE187E9C582BA6'
#
# hashObject = hashlib.sha3_256()
# hashObject.update(publicKey)
# hex_dig = hashObject.hexdigest()
# print(hex_dig)
#
# prefix = b'0x04'
# print(binascii.hexlify(prefix))
# print(prefix.hex())
#
# print(bin(3))


privateKeyHex = '0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'

#####################################################################
# Add 0x80 byte to the front
#####################################################################

hexByte = '80' # each hexadecimal digit represents a nibble (4 bits) 0x is the prefix so you have 80 which is 8 bits = 1 byte
extendedKey = hexByte + privateKeyHex

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(binascii.unhexlify(hash_string)).hexdigest()
    return sha_signature

first_sha256 = encrypt_string(extendedKey)
print(first_sha256)
second_sha256 = encrypt_string(first_sha256)
print(second_sha256)

# add checksum to end of extended key (4 bytes so 8 hex characters)
final_key = extendedKey + second_sha256[:8]
print(final_key)

# Wallet Import Format = base 58 encoded final_key
WIF = base58.b58encode(binascii.unhexlify(final_key))
print(WIF)


import hashlib
import base58
import binascii

private_key_WIF = '5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
first_encode = base58.b58decode(private_key_WIF)
print (binascii.hexlify(first_encode))