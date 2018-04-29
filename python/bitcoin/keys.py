import os
import binascii

private_key_byte = os.urandom(32)
private_key = binascii.hexlify(private_key_byte)
print(private_key_byte)
print(private_key)