import random

def generatePrivateKey():
    privateKeyArray = []
    for i in range(0, 256):
        bit = random.randint(1,100)
        if bit > 50:
            bit = 1
        else:
            bit = 0
        privateKeyArray.append(str(bit))

    privateKeyBinary = int(''.join(privateKeyArray))
    privateKeyDecimal = int(str(privateKeyBinary), 2)
    privateKeyHex = hex(privateKeyDecimal)


    if privateKeyDecimal > 115792089237316195423570985008687907852837564279074904382605163141518161494336 or privateKeyDecimal < 0:
        raise Exception("Private key generation not in range please retry")

    print("Private Key Binary: " + str(privateKeyBinary))
    print("Private Key Decimal: " + str(privateKeyDecimal))
    print("Private Key Hex: " + str(privateKeyHex))

    return int(privateKeyHex, 16)

generatePrivateKey()