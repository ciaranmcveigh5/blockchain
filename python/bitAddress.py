import hashlib
import binascii
import base58

privateKey = '95467a77de3729968fc03762ce2e77358721b5783b374da45ac0293e350fd1b5'
publicKey = binascii.unhexlify('047FB31690807787D04E81F5C82D611C30A42536A1F256D041652BEEF96C2DA8C0C734049FD31A7457D975A2175D0FFBA04EE078CB6A060C7DC8A73144FBBB86A6')

def sha_256(bytes):
    return hashlib.sha256(bytes).digest()

def ripemd_160(bytes):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(bytes)
    return ripemd160.digest()

# SHA-256(Public_Key)

sha_256_hash = sha_256(publicKey)
print("SHA-256(Public_Key) = " + str(binascii.hexlify(sha_256_hash).decode("utf-8")))

# RIPEMD-160(SHA-256(Public_Key))

ripemd_160_hash = ripemd_160(sha_256_hash)
print("RIPEMD-160(SHA-256(Public_Key)) = " + str(binascii.hexlify(ripemd_160_hash).decode("utf-8")))

# PREFIX + RIPEMD-160(SHA-256(Public_Key))

prefix = binascii.unhexlify('00')
address = prefix + ripemd_160_hash
print("PREFIX + RIPEMD-160(SHA-256(Public_Key)) = " + str(binascii.hexlify(address).decode("utf-8")))

# Double SHA-256 and Checksums

double_sha_256 = sha_256(sha_256(address))
print("SHA-256(SHA-256(REFIX + RIPEMD-160(SHA-256(Public_Key)))) = " + str(binascii.hexlify(double_sha_256).decode("utf-8")))
checksum = double_sha_256[:4]
print("CHECKSUM = " + str(binascii.hexlify(checksum).decode("utf-8")))
address = prefix + ripemd_160_hash + checksum
print("PREFIX + RIPEMD-160(SHA-256(Public_Key)) + CHECKSUM = " + str(binascii.hexlify(address).decode("utf-8")))

# Base 58 Encoding

bitcoin_address = base58.b58encode(address)
print("BASE_58(PREFIX + RIPEMD-160(SHA-256(Public_Key)) + CHECKSUM) = " + str(bitcoin_address.decode("utf-8")))
print("BITCOIN ADDRESS = " + str(bitcoin_address.decode("utf-8")))

