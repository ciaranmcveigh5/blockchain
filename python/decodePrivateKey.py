import random

privateKey = 'L33tTQ7otgXRzMZ7AP19zxT2oAUxN6feSA54q8JwouTWrEZjH4mq'
bitcoinAddress = '1DXgDfzi1wLTwxYbzonNvrkfnFK5LNfkXm'

pkb = '1110111100100011010110101010110011111001000011011001111101001010101011011101100011001001001011100100101100100101011000101110000111011001111010111001011111110000110111111001101110100011101101010000100000100101100001110011100111001011000000010011110110110010'




#####################################################################
# Convert hex to decimal
#####################################################################

# privateKeyDecimal = int(privateKey, 16)
# print(privateKeyDecimal)
# privateKeyBinary = bin(privateKeyDecimal)
# print(privateKeyBinary)



number = 11111111111111222312121321321132312245
numberHex = hex(number)
print(numberHex)
i = int(numberHex, 16)
print(i)
print(bin(i))

b512 = '1000000000000'
i512 = int(b512, 2)

print(i512)

# binaryArray = list(b512)
# print(binaryArray)
#
# print(len(binaryArray))
# reversedBinaryArray = reversed(binaryArray)
# print(reversedBinaryArray)
# print(list(reversedBinaryArray))


def binaryToDecimal(binary):
    binaryArray = list(binary)
    reversedBinaryArrayObject = reversed(binaryArray)
    reversedBinaryArray = list(reversedBinaryArrayObject)
    decimal = 0
    for i in range(0, len(reversedBinaryArray)):
        # print(int(reversedBinaryArray[i]))
        # print(i)
        # print(2**i)
        if int(reversedBinaryArray[i]) == 1:
            decimal += 2**i
    return decimal

print(binaryToDecimal('1000000000000'))
pkd = binaryToDecimal(pkb)
print(pkd)
pkh = hex(pkd)
pkh2 = format(pkd, 'x')
if (pkd < 10**77):
    print('true')
print(pkh)
print(pkh2)

a = 0b101
b = 0b011
c = a^b
print(c)

hex5 = '0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140'
hex6 = int(hex5, 16)

hex7 = '0x1'
hex8 = int(hex7, 16)

print(hex8)

print(hex6)
print(10**77)

print(random.randint(0, hex6))
#####################################################################
# Convert hex to binary
#####################################################################

#####################################################################
# Generate public key
#####################################################################


