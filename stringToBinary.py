#####################################################################
# Get input from user
#####################################################################

phrase = input('Phrase to convert to binary: ')

#####################################################################
# Split phrase into array of characters
#####################################################################

characterArray = list(phrase)

asciiArray = []
binaryArray = []

#####################################################################
# Convert characters to ascii numbers
#####################################################################

for character in characterArray:
    asciiNumber = ord(character) # see https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html for reference
    asciiArray.append(asciiNumber)

#####################################################################
# Convert ascii numbers to binary
#####################################################################

for number in asciiArray:
    eightBitBinary = format(number, '08b')
    binaryArray.append(eightBitBinary)

#####################################################################
# Concatenate binary numbers
#####################################################################

binaryOutput = ''.join(binaryArray)

print(characterArray)
print(asciiArray)
print(binaryArray)
print(binaryOutput)


