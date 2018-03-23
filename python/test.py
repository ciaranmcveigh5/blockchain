
import hashlib
import pickle

transactions = ['a', 'b', 'c']

m = hashlib.sha3_256()

def hash_transactions(transactions):
    hashed_transactions = []
    for tx in transactions:
        m = hashlib.sha3_256()
        pickle_tx = pickle.dumps(tx)
        print(pickle_tx)
        m.update(tx.encode())
        hashed_transactions.append(m.hexdigest())
    return hashed_transactions

def chunk_transactions(hashed_transactions):
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
        joined_hashes = ''.join(two_set)
    else:
        new_array = two_set * 2
        joined_hashes = ''.join(new_array)
    return joined_hashes


def get_merkle_root(transactions):
    print(transactions)
    while len(transactions) > 1:
        transactions = chunk_transactions(hash_transactions(transactions))
    return transactions

print(get_merkle_root(transactions))

for x in transactions:
    print(x)
    m.update(x.encode())
    print(m.hexdigest())

m = hashlib.sha3_256()
m.update('80084bf2fba02475726feb2cab2d8215eab14bc6bdd8bfb2c8151257032ecd8bb039179a8a4ce2c252aa6f2f25798251c19b75fc1508d9d511a191e0487d64a7'.encode())
# print('a')
# print(b'a')
print(m.hexdigest())

x1 = 'a'.encode()
x2 = pickle.dumps('a')
x3 = pickle.dumps('a', 1)

print('--------------------------------')
print(x1)
print(x2)
print(x3)

# x1 = {'a': '80084bf2fba02475726feb2cab2d8215eab14bc6bdd8bfb2c8151257032ecd8bb039179a8a4ce2c252aa6f2f25798251c19b75fc1508d9d511a191e0487d64a7', 'b': 'b'}.encode()
x2 = pickle.dumps({'a': '80084bf2fba02475726feb2cab2d8215eab14bc6bdd8bfb2c8151257032ecd8bb039179a8a4ce2c252aa6f2f25798251c19b75fc1508d9d511a191e0487d64a7', 'b': 'b'})

print('--------------------------------')
print(x1)
print(x2)
#
# m = hashlib.sha3_256()
# m.update('a'.encode())
# print('a')
# print('a'.encode())
# print(m.digest())
#
# m.update('a'.encode())
# print('a')
# print('a'.encode())
# print(m.digest())
#
# m = hashlib.sha3_256()
#
# m.update('aa'.encode())
# print('aa')
# print('aa'.encode())
# print(m.digest())
#
# mystring = 'a'
# b = mystring.encode('utf-8')
# print(b)

# print(chunk_transactions(hash_transactions(transactions)))

# from hashlib import sha256 as sha
#
# def chunks(l, n):
#     """Yield successive n-sized chunks from l."""
#     # result = []
#     for i in range(0, len(l), n):
#         # result.append(l[i:i + n])
#         yield l[i:i + n]
#     # return result
#
# def m_tree(transactions):
#     """Takes an array of transactions and computes a Merkle root"""
#     sub_t = []
#     for i in chunks(transactions, 2):
#         if len(i) == 2:
#             hash = sha(str(i[0]+i[1])).hexdigest()
#         else:
#             hash = sha(str(i[0]+i[0])).hexdigest()
#         sub_t.append(hash)
#     print(sub_t)
#     if len(sub_t) == 1:
#        return sub_t[0]
#     else:
#        return m_tree(sub_t)
#
#
# print(chunks({1, 2, 3}, 4))
#
# # print(m_tree({{'1': 'a'}, {'2': 'b'}, {'3': 'f'}, {'4': 'k'}}))
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range (0, len(x), 2):
#     print(x[0:5:4])
#
# x2 = ['a', 'b']
# tx = [
#         {
#             'from': 'A',
#             'to': 'B',
#             'amount': 10
#         },
#         {
#             'from': 'B',
#             'to': 'C',
#             'amount': 10
#         },
#         {
#             'from': 'C',
#             'to': 'D',
#             'amount': 10
#         }
#     ]
#
# # sha.update(tx[0])
# # print(sha.digest())
#
# hash = sha(b'hello world').digest
# sub_t = []
# sub_t.append(hash)
# print(sub_t)
# print(sha(str(x2[0]+x2[1])).hexdigest())

# # 0. Import the needed library
# import hashlib, json
# from collections import OrderedDict
#
#
# # 1. Declare the class trees
# class Jae_MerkTree:
#
#     # 2. Initiate the class object
#     def __init__(self, listoftransaction=None):
#         self.listoftransaction = listoftransaction
#         self.past_transaction = OrderedDict()
#
#     # 3. Create the Merkle Tree
#     def create_tree(self):
#
#         # 3.0 Continue on the declaration
#         listoftransaction = self.listoftransaction
#         past_transaction = self.past_transaction
#         temp_transaction = []
#
#         # 3.1 Loop until the list finishes
#         for index in range(0, len(listoftransaction), 2):
#
#             # 3.2 Get the most left element
#             current = listoftransaction[index]
#
#             # 3.3 If there is still index left get the right of the left most element
#             if index + 1 != len(listoftransaction):
#                 current_right = listoftransaction[index + 1]
#
#             # 3.4 If we reached the limit of the list then make a empty string
#             else:
#                 current_right = ''
#
#             # 3.5 Apply the Hash 256 function to the current values
#             current_hash = hashlib.sha256(current)
#
#             # 3.6 If the current right hash is not a '' <- empty string
#             if current_right != '':
#                 current_right_hash = hashlib.sha256(current_right)
#
#             # 3.7 Add the Transaction to the dictionary
#             past_transaction[listoftransaction[index]] = current_hash.hexdigest()
#
#             # 3.8 If the next right is not empty
#             if current_right != '':
#                 past_transaction[listoftransaction[index + 1]] = current_right_hash.hexdigest()
#
#             # 3.9 Create the new list of transaction
#             if current_right != '':
#                 temp_transaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())
#
#             # 3.01 If the left most is an empty string then only add the current value
#             else:
#                 temp_transaction.append(current_hash.hexdigest())
#
#         # 3.02 Update the variables and rerun the function again
#         if len(listoftransaction) != 1:
#             self.listoftransaction = temp_transaction
#             self.past_transaction = past_transaction
#
#             # 3.03 Call the function repeatly again and again until we get the root
#             self.create_tree()
#
#     # 4. Return the past Transaction
#     def Get_past_transacion(self):
#         return self.past_transaction
#
#     # 5. Get the root of the transaction
#     def Get_Root_leaf(self):
#         last_key = self.past_transaction.keys()[-1]
#         return self.past_transaction[last_key]
#
#
# # Declare the main part of the function to run
# if __name__ == "__main__":
#     # a) Create the new class of Jae_MerkTree
#     Jae_Tree = Jae_MerkTree()
#
#     # b) Give list of transaction
#     transaction = ['a', 'b', 'c', 'd']
#
#     # c) pass on the transaction list
#     Jae_Tree.listoftransaction = transaction
#
#     # d) Create the Merkle Tree transaction
#     Jae_Tree.create_tree()
#
#     # e) Retrieve the transaction
#     past_transaction = Jae_Tree.Get_past_transacion()
#
#     # f) Get the last transaction and print all
#     print
#     "First Example - Even number of transaction Merkel Tree"
#     print
#     'Final root of the tree : ', Jae_Tree.Get_Root_leaf()
#     print(json.dumps(past_transaction, indent=4))
#     print
#     "-" * 50
#
#     # h) Second example
#     print
#     "Second Example - Odd number of transaction Merkel Tree"
#     Jae_Tree = Jae_MerkTree()
#     transaction = ['a', 'b', 'c', 'd', 'e']
#     Jae_Tree.listoftransaction = transaction
#     Jae_Tree.create_tree()
#     past_transaction = Jae_Tree.Get_past_transacion()
#     print
#     'Final root of the tree : ', Jae_Tree.Get_Root_leaf()
#     print(json.dumps(past_transaction, indent=4))
#     print
#     "-" * 50
#
#     # i) Actual Use Case
#     print
#     "Final Example - Actuall use case of the Merkle Tree"
#
#     # i-1) Declare a transaction - the ground truth
#     ground_truth_Tree = Jae_MerkTree()
#     ground_truth_transaction = ['a', 'b', 'c', 'd', 'e']
#     ground_truth_Tree.listoftransaction = ground_truth_transaction
#     ground_truth_Tree.create_tree()
#     ground_truth_past_transaction = ground_truth_Tree.Get_past_transacion()
#     ground_truth_root = ground_truth_Tree.Get_Root_leaf()
#
#     # i-2) Declare a tampered transaction
#     tampered_Tree = Jae_MerkTree()
#     tampered_Tree_transaction = ['a', 'b', 'c', 'd', 'f']
#     tampered_Tree.listoftransaction = tampered_Tree_transaction
#     tampered_Tree.create_tree()
#     tampered_Tree_past_transaction = tampered_Tree.Get_past_transacion()
#     tampered_Tree_root = tampered_Tree.Get_Root_leaf()
#
#     # i-3) The three company share all of the transaction
#     print
#     'Company A - my final transaction hash : ', ground_truth_root
#     print
#     'Company B - my final transaction hash : ', ground_truth_root
#     print
#     'Company C - my final transaction hash : ', tampered_Tree_root
#
#     # i-4) Print out all of the past transaction
#     print
#     "\n\nGround Truth past Transaction "
#     print(json.dumps(ground_truth_past_transaction, indent=4))
#
#     print
#     "\n\nTamper Truth past Transaction "
#     print(json.dumps(tampered_Tree_past_transaction, indent=4))
#
# # ---- END OF THE CODE ------