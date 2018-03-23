import hashlib
import pickle

transactions = [
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
        },
        {
            'from': 'D',
            'to': 'E',
            'amount': 10
        },
        {
            'from': 'E',
            'to': 'F',
            'amount': 10
        },
        {
            'from': 'F',
            'to': 'G',
            'amount': 10
        },
        {
            'from': 'G',
            'to': 'H',
            'amount': 10
        }
    ]



def hash_transactions(transactions):
    hashed_transactions = []
    for tx in transactions:
        m = hashlib.sha3_256()
        pickle_tx = pickle.dumps(tx) # Convert JSON element to byte form
        print(pickle_tx)
        m.update(pickle_tx)
        hashed_transactions.append(m.hexdigest()) # hash the byte data and add to hashed_transactions array
    return hashed_transactions

def chunk_transactions(hashed_transactions): # split transactions in separate arrays of length 2
    new_hashes = []
    for i in range(0, len(hashed_transactions), 2):
        two_set = hashed_transactions[i:i + 2]
        joined_hashes = join_hashes(two_set)
        new_hashes.append(joined_hashes)
    print(new_hashes)
    new_hashes = hash_transactions(new_hashes)
    print(new_hashes)
    return new_hashes

def join_hashes(two_set):
    if len(two_set) == 2:
        joined_hashes = ''.join(two_set) # if chunk has 2 items concatenate these 2 hashes
    else:
        new_array = two_set * 2
        joined_hashes = ''.join(new_array) # if chunk has 1 item then duplicate the hash and concatenate
    return joined_hashes


def get_merkle_root(transactions):
    print(transactions)
    while len(transactions) > 1:
        transactions = chunk_transactions(hash_transactions(transactions)) # recursively hash and concatenate txs until a single hash is obtained
    return transactions


print('Merkle Root: ' + str(get_merkle_root(transactions)))