import binascii

a = 'ABC'
byte_a = bytes(a, encoding='utf')
print(byte_a)
# binary = bin(ord(a))[2:]
# print(binary)
# print(binary.encode())
b = binascii.hexlify(byte_a)
print('b = ', b)

c = int(b, 16)
print('c = ', c)

d = hex(c)[2:]
print('d = ', d)
print(d.encode())

e = binascii.unhexlify(d.encode())
print('e = ', e)

f = e.decode()
print('f = ', f)

hash3 = b'0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D'
hash4 = binascii.unhexlify(hash3)
print(hash4)
hash5 = binascii.hexlify(hash4)
print(hash5)

test1 = b'\x0c'
test2 = binascii.hexlify(test1)
print(test2)
print(chr(0x0a))

test3 = b'/'
test4 = binascii.hexlify(test3)
print(test4)

