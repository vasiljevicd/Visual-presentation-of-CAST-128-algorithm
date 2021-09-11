from bitarray import bitarray


def splitPlainOrCipherText(plaintext):
    binaryPlainText = plainOrCipherTextHexToBinary(plaintext)
    leftside = binaryPlainText[0:32]
    rightside = binaryPlainText[32:64]

    return leftside, rightside


def plainOrCipherTextHexToBinary(plaintextHex):
    h_size = len(plaintextHex) * 4
    int_value = (int(plaintextHex, 16))
    plaintextString = (bin(int_value)[2:]).zfill(64)
    binaryPlaintext = bitarray(plaintextString)
    return binaryPlaintext


def getPlainOrCipherText(plainOrCipherTextHex):
    h_size = len(plainOrCipherTextHex) * 4
    return h_size


def checkPlainOrCipherText(plainOrCipherText):
    try:
        int_value = (int(plainOrCipherText, 16))
        return True
    except ValueError:
        return False
