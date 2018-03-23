def binaryToDecimal(binary):
    validityArray = ['0', '1']
    binaryArray = list(str(binary))
    reversedBinaryArray = list(reversed(binaryArray))
    decimal = 0
    for i in range (0, len(reversedBinaryArray)):
        if reversedBinaryArray[i] not in validityArray:
            return 'Invalid Binary Input'
        decimal += (int(reversedBinaryArray[i]) * 2**i)

    return decimal

def hexToDecimal(hex):
    validityArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexDictionary = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hexUpper = hex.upper()
    hexArray = list(str(hexUpper))
    reversedHexArray = list(reversed(hexArray))
    decimal = 0
    for i in range (0, len(reversedHexArray)):
        if reversedHexArray[i] not in validityArray:
            return 'Invalid Hex Input'
        decimal += (hexDictionary[reversedHexArray[i]] * 16**i)

    return decimal

def decimalToBinary(decimal):
    bitArray = []
    result = decimal
    while result != 0:
        if result % 2 == 0:
            bitArray.append(0)
        else:
            bitArray.append(1)
        result = result // 2
    bitArrayString = [str(i) for i in bitArray]
    return "".join(list(reversed(bitArrayString)))

def decimalToHex(decimal):
    hexArray = []
    hexDictionary = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }
    result = decimal
    while result != 0:
        remainder = result % 16
        hexArray.append(hexDictionary[str(remainder)])
        result = result // 16 # floor division also known as integer division
    return "".join(list(reversed(hexArray)))

def binaryToBytes(binary):
    return 'TODO'

def binaryToHex(binary):
    return 'TODO'

def binaryToAscii(binary):
    asciiDictionary = {i: chr(i) for i in range(129)} # see https://www.asciitable.com/ for table
    n = 8
    asciiArray = []
    byteArray = [str(binary)[i:i+n] for i in range(0, len(str(binary)), n)]
    print(byteArray)
    decimalArray = [binaryToDecimal(i) for i in byteArray]
    print(decimalArray)
    for number in decimalArray:
        asciiArray.append(asciiDictionary[number])
    return "".join(list(asciiArray))


print(binaryToDecimal(10011010))
print(hexToDecimal('ba0de'))
print(decimalToBinary(154))
print(decimalToHex(762078))
print({i: chr(i) for i in range(129)})
print(binaryToAscii('01001000011001010110110001101100011011110010000001110111011001010110110001100011011011110110110101100101001000000111010001101111001000000100001001101100011011110110001101101011011000110110100001100001011010010110111000100000010101000110010101100011011010000110111001101111011011000110111101100111011010010110010101110011'))

# test it here https://www.rapidtables.com/convert/number/binary-to-decimal.html 

