import hashlib
import pickle
import random


# Block Structure

block = {
    'previousBlockHeader': 'effb6c85c6ee147a0f6813f1f6b6f12ffed373cef37a47cd59f4945427872f3d',
    'nonce': 0,
    'transactions': [ # In reality this array of transaction would be captured in a single hash known as the merkle root
        {
            'from': 'Anthony', # From and To would actually be bitcoin addresses
            'to': 'Bill',
            'amount': 10
        },
        {
            'from': 'Bill',
            'to': 'Charles',
            'amount': 10
        },
        {
            'from': 'Charles',
            'to': 'Damien',
            'amount': 10
        }
    ]
}

# Set up, converting json to byte output and hashing that byte output

hashed_block = pickle.dumps(block)
m = hashlib.sha256(hashed_block)

# Set difficulty, the difficultly relates to the required number of 0's at the beginning of the hash, the more 0's the harder the problem

difficulty = 2
difficulty_string = ''.join(['0' for x in range(difficulty)])

difficulty_hash = 0x00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
difficult_decimal = 452312848583266388373324160190187140051835877600158453279131187530910662655


# Set Miners involved and their respective CPU's

alice = 3 * ['Alice'] # Represents 3 cpu units for alice
bob = 5 * ['Bob'] # Represents 5 cpu units for bob
charlie = 10 * ['Charlie'] # Represents 10 cpu units for charlie
deborah = 1 * ['Deborah'] # Represents 1 cpu unit for deborah

# Add Miners to an array and shuffle

cpus = [alice, bob, charlie, deborah]
miners = []
for cpu in cpus:
    miners.extend(cpu)
random.shuffle(miners)

# While the hash does not have the desired beginning of 0 try a different nonce

while m.hexdigest()[:difficulty] != difficulty_string:
    block['nonce'] += 1 # Increment nonce (ie change your guess)
    m = hashlib.sha256(pickle.dumps(block)) # Convert data to byte form so it can be hashed
    print('Nonce Guess: ' + str(block['nonce']))
    print('Resultant Hash: ' + str(m.hexdigest()))
    print('Decimal value of hash: ' + str(int(m.hexdigest(), 16)))
    if int(m.hexdigest(), 16) < difficulty_hash:
        print('Valid Hash: ' + str(int(m.hexdigest(), 16)) + ' is less than ' + str(difficulty_hash))
    miner = miners[block['nonce'] % len(miners)] # The miner who mined the block
    blockheader = m.hexdigest() # The hash of the block and nonce which will be the blockheader for that block

print('Miner who Mined Block: ' + miner)