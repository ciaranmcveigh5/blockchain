import hashlib
import binascii
import pickle
import random

# Hashing Explained

m = hashlib.sha3_256()

m.update(b'hello world')

hash1 = m.digest()
hash2 = m.hexdigest()
hash3 = binascii.unhexlify(hash2)


print(m.digest())
print(m.hexdigest())
print(hash3)

# Block Structure Explained

block = {
    'previousBlockHeader': hash2,
    'nonce': 0,
    'transactions': [
        {
            'from': 'A',
            'to': 'B',
            'amount': 10
        },
        {
            'from': 'B',
            'to': 'C',
            'amount': 10
        },
        {
            'from': 'C',
            'to': 'D',
            'amount': 10
        }
    ]
}

blockchain = pickle.dumps(block)

m.update(blockchain)
blockheader = m.digest()

print(blockheader)

print(bin(int(hash2, base=16)))

# Mining Nonce Explained

difficulty = 2
difficulty_string = ''.join(['0' for x in range(difficulty)])
nonce = 1
block['nonce'] = 1

# while m.hexdigest()[:difficulty] != difficulty_string:
#     nonce += 1
#     block['nonce'] = nonce
#     m = hashlib.sha3_256()
#     m.update(pickle.dumps(block))
#     print(nonce)
#     print(m.hexdigest())
#     miners = ['Alice', 'Bob', 'Charlie', 'Deborah', 'Evan', 'Frank']
#     miner = miners[nonce % len(miners)]
#
# print(miner)

while m.hexdigest()[:difficulty] != difficulty_string:
    nonce += 1
    block['nonce'] = nonce
    m = hashlib.sha3_256()
    m.update(pickle.dumps(block))
    print(nonce)
    print(m.hexdigest())
    alice = 3 * ['Alice'] # represents 3 cpu units for alice
    bob = 5 * ['Bob'] # represents 5 cpu units for bob
    charlie = 10 * ['Charlie'] # represents 10 cpu units for charlie
    deborah = 1 * ['Deborah'] # represents 1 cpu unit for deborah
    cpus = [alice, bob, charlie, deborah]
    miners = []
    for cpu in cpus:
        miners.extend(cpu)
    random.shuffle(miners)
    miner = miners[nonce % len(miners)]

print(miner)

