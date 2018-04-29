import hashlib
import pickle
import random
import time


# Block Structure, note in reality there are a number of different variables in the blockheader see https://bitcoin.org/en/developer-reference#block-headers for more info

block_header = {
    'previousBlockHash': 'effb6c85c6ee147a0f6813f1f6b6f12ffed373cef37a47cd59f4945427872f3d',
    'height': 1,
    'difficulty': 452312848583266388373324160190187140051835877600158453279131187530910662655,
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

hashed_block = pickle.dumps(block_header)
m = hashlib.sha256(hashed_block)

# Set difficulty, the difficulty_hash below is the equivalent of requiring 2 zeros at the front of the hash

difficulty_hash = 0x00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
difficult_decimal = 452312848583266388373324160190187140051835877600158453279131187530910662655


# Set Miners involved and their respective CPU's

alice = 3 * ['Alice'] # Represents 3 cpu units for alice
bob = 5 * ['Bob'] # Represents 5 cpu units for bob
charlie = 10 * ['Charlie'] # Represents 10 cpu units for charlie
deborah = 1 * ['Deborah'] # Represents 1 cpu unit for deborah

# Add Miners to an array and shuffle

elapsed_time = 0

cpus = [alice, bob, charlie, deborah]
miners = []
for cpu in cpus:
    miners.extend(cpu)
random.shuffle(miners)

def is_new_difficulty_outside_factor_of_four(new_difficulty, old_difficulty):
    if new_difficulty > (old_difficulty * 4) or new_difficulty < (old_difficulty/4):
        return True
    else:
        return False

def set_difficulty_to_factor_of_four(new_difficulty, old_difficulty):
    if new_difficulty > old_difficulty:
        new_difficulty = old_difficulty * 4
    else:
        new_difficulty = old_difficulty / 4
    return new_difficulty

def recalculate_difficulty(old_difficulty, current_block_rate):
    new_difficulty = old_difficulty * (current_block_rate/10)
    if is_new_difficulty_outside_factor_of_four(new_difficulty, old_difficulty):
        new_difficulty = set_difficulty_to_factor_of_four(new_difficulty, old_difficulty)
    return new_difficulty

# While the hash is bigger than or equal to the difficulty continue to iterate the nonce
blocks = []
start_time = time.time()
start_time_single_block = time.time()

while block_header['height'] < 100:
    while int(m.hexdigest(), 16) >= block_header['difficulty']:
        block_header['nonce'] += 1 # Increment nonce (ie change your guess)
        m = hashlib.sha256(pickle.dumps(block_header)) # Convert data to byte form so it can be hashed
        # print('Nonce Guess: ' + str(block_header['nonce']))
        # print('Resultant Hash: ' + str(m.hexdigest()))
        # print('Decimal value of hash: ' + str(int(m.hexdigest(), 16)) + '\n')
        miner = miners[block_header['nonce'] % len(miners)] # The miner who mined the block
        block_hash = m.hexdigest() # The hash of the blockheader with that nonce yields the block hash for that block
    elapsed_time_single_block = time.time() - start_time_single_block
    start_time_single_block = time.time()
    if block_header['height'] % 10 == 0:
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        block_header['difficulty'] = recalculate_difficulty(block_header['difficulty'], elapsed_time)
        start_time = time.time()
    block_header['height'] += 1
    print(block_header['height'])
    hashed_block = pickle.dumps(block_header)
    m = hashlib.sha256(hashed_block)
    blocks.append({
        'height': block_header['height'],
        'difficuly': block_header['difficulty'],
        'miner': miner,
        'time': elapsed_time_single_block
    })

print(blocks)