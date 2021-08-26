from bitarray import bitarray

from UI.errorDialog import ErrorDialog
from core.sboxes import calculatingSboxOutput


def keyGenerator(keyBinary):
    keysArray = [None] * 32

    for i in range(4):
        z = calculateZ(keyBinary)
        z1 = divideKeyTo16Parts(z)
        if i == 0 or i == 2:
            calculateKeys1(keysArray, z1, i)
        elif i == 1 or i == 3:
            calculateKeys3(keysArray, z1, i)
        keyBinary = calculateBinaryKey(z, z1, keyBinary)
        x = divideKeyTo16Parts(keyBinary)
        if i == 0 or i == 2:
            calculateKeys2(keysArray, x, i)
        elif i == 1 or i == 3:
            calculateKeys4(keysArray, x, i)

    return generateMaskingAndRotationKeys(keysArray)


def keyHexToBinary(keyHex):
    # fale errors za nevalidne ulaze, vecu velicinu kljuca
    h_size = len(keyHex) * 4

    # ako kljuc nema 128 bita, dodaju se na desnu stranu 0
    if h_size < 128:
        int_value = (int(keyHex, 16)) << (128 - h_size)
    else:
        int_value = (int(keyHex, 16))
    binaryKeyString = (bin(int_value)[2:]).zfill(128)
    binaryKey = bitarray(binaryKeyString)
    if 80 < h_size <= 128:
        numberOfRounds = 16
    else:
        numberOfRounds = 12
    return binaryKey, numberOfRounds


def getKeySize(keyHex):
    h_size = len(keyHex) * 4
    return h_size


def checkKeyFormat(keyHex):
    try:
        (int(keyHex, 16))
        return True
    except ValueError:
        return False


def divideKeyTo16Parts(keyBinary):
    x = []
    for i in range(16):
        x.append(keyBinary[i * 8:(i + 1) * 8])
    print(x)
    return x


def divideKeyTo8Parts(keyBinary):
    x = []
    print("binary ", keyBinary)
    for i in range(8):
        x.append(keyBinary[i * 4:(i + 1) * 4])
    print("x", x)
    return x


def calculateZ(keyBinary):
    z = bitarray(128)
    z[:] = 0
    x = divideKeyTo16Parts(keyBinary)
    # z0z1z2z3 =          x0x1x2x3 ^                        S5[xD] ^                          S6[xF] ^ S7[xC] ^ S8[xE] ^ S7[x8]
    z[0:32] = keyBinary[0:32] ^ calculatingSboxOutput(5, x[13]) ^ calculatingSboxOutput(6, x[15]) \
              ^ calculatingSboxOutput(7, x[12]) ^ calculatingSboxOutput(8, x[14]) ^ calculatingSboxOutput(7, x[8])

    z1 = divideKeyTo16Parts(z)
    print('z', z)
    # z4z5z6z7 = x8x9xAxB ^ S5[z0] ^ S6[z2] ^ S7[z1] ^ S8[z3] ^ S8[xA]
    z[32:64] = keyBinary[64:96] ^ calculatingSboxOutput(5, z1[0]) ^ calculatingSboxOutput(6, z1[2]) \
               ^ calculatingSboxOutput(7, z1[1]) ^ calculatingSboxOutput(8, z1[3]) ^ calculatingSboxOutput(8, x[10])

    z1 = divideKeyTo16Parts(z)
    print('z', z)
    # z8z9zAzB = xCxDxExF ^ S5[z7] ^ S6[z6] ^ S7[z5] ^ S8[z4] ^ S5[x9]
    z[64:96] = keyBinary[96:128] ^ calculatingSboxOutput(5, z1[7]) ^ calculatingSboxOutput(6, z1[6]) \
               ^ calculatingSboxOutput(7, z1[5]) ^ calculatingSboxOutput(8, z1[4]) ^ calculatingSboxOutput(5, x[9])

    z1 = divideKeyTo16Parts(z)
    print('z', z)
    # zCzDzEzF = x4x5x6x7 ^ S5[zA] ^ S6[z9] ^ S7[zB] ^ S8[z8] ^ S6[xB]
    z[96:128] = keyBinary[32:64] ^ calculatingSboxOutput(5, z1[10]) ^ calculatingSboxOutput(6, z1[9]) \
                ^ calculatingSboxOutput(7, z1[11]) ^ calculatingSboxOutput(8, z1[8]) ^ calculatingSboxOutput(6,
                                                                                                             x[11])
    return z


def calculateBinaryKey(z, z1, keyBinary):
    # x0x1x2x3 =            z8z9zAzB     ^                 S5[z5] ^                       S6[z7] ^                               S7[z4] ^                      S8[z6] ^                          S7[z0]
    keyBinary[0:32] = z[64:96] ^ calculatingSboxOutput(5, z1[5]) ^ calculatingSboxOutput(6, z1[
        7]) ^ calculatingSboxOutput(7, z1[4]) ^ calculatingSboxOutput(8, z1[6]) ^ calculatingSboxOutput(7, z1[0])

    x = divideKeyTo16Parts(keyBinary)

    # x4x5x6x7 =             z0z1z2z3 ^                      S5[x0] ^                          S6[x2] ^                     S7[x1] ^                            S8[x3] ^                      S8[z2]
    keyBinary[32:64] = z[0:32] ^ calculatingSboxOutput(5, x[0]) ^ calculatingSboxOutput(6, x[
        2]) ^ calculatingSboxOutput(7, x[1]) ^ calculatingSboxOutput(8, x[3]) ^ calculatingSboxOutput(8, z1[2])

    x = divideKeyTo16Parts(keyBinary)

    #    x8x9xAxB =         z4z5z6z7 ^                          S5[x7] ^                         S6[x6] ^                          S7[x5] ^                      S8[x4] ^                       S5[z1]
    keyBinary[64:96] = z[32:64] ^ calculatingSboxOutput(5, x[7]) ^ calculatingSboxOutput(6, x[
        6]) ^ calculatingSboxOutput(7, x[5]) ^ calculatingSboxOutput(8, x[4]) ^ calculatingSboxOutput(5, z1[1])

    x = divideKeyTo16Parts(keyBinary)

    # xCxDxExF =              zCzDzEzF ^                           S5[xA] ^                        S6[x9] ^                          S7[xB] ^                      S8[x8] ^                          S6[z3]
    keyBinary[96:128] = z[96:128] ^ calculatingSboxOutput(5, x[10]) ^ calculatingSboxOutput(6, x[
        9]) ^ calculatingSboxOutput(7, x[11]) ^ calculatingSboxOutput(8, x[8]) ^ calculatingSboxOutput(6, z1[3])

    return keyBinary


def calculateKeys1(keysArray, z1, i):
    # K1  =                                 S5[z8] ^                       S6[z9] ^                           S7[z7] ^                      S8[z6] ^                         S5[z2]
    keysArray[i * 8 + 0] = calculatingSboxOutput(5, z1[8]) ^ calculatingSboxOutput(6, z1[9]) ^ calculatingSboxOutput(7,
                                                                                                                     z1[
                                                                                                                         7]) \
                           ^ calculatingSboxOutput(8, z1[6]) ^ calculatingSboxOutput(5, z1[2])

    # K2  =                               S5[zA] ^                           S6[zB] ^                           S7[z5] ^                         S8[z4] ^                         S6[z6]
    keysArray[i * 8 + 1] = calculatingSboxOutput(5, z1[10]) ^ calculatingSboxOutput(6, z1[11]) ^ calculatingSboxOutput(
        7, z1[5]) \
                           ^ calculatingSboxOutput(8, z1[4]) ^ calculatingSboxOutput(6, z1[6])

    # K3  =                               S5[zC] ^                           S6[zD] ^                           S7[z3] ^                           S8[z2] ^                         S7[z9]
    keysArray[i * 8 + 2] = calculatingSboxOutput(5, z1[12]) ^ calculatingSboxOutput(6, z1[13]) ^ calculatingSboxOutput(
        7, z1[3]) \
                           ^ calculatingSboxOutput(8, z1[2]) ^ calculatingSboxOutput(7, z1[9])

    # K4  =                               S5[zE] ^                           S6[zF] ^                          S7[z1] ^                          S8[z0] ^                           S8[zC]
    keysArray[i * 8 + 3] = calculatingSboxOutput(5, z1[14]) ^ calculatingSboxOutput(6, z1[15]) ^ calculatingSboxOutput(
        7, z1[1]) \
                           ^ calculatingSboxOutput(8, z1[0]) ^ calculatingSboxOutput(8, z1[12])


def calculateKeys2(keysArray, x, i):
    #                                          S5[x3] ^                          S6[x2] ^                      S7[xC] ^ S8[xD] ^ S5[x8
    keysArray[i * 8 + 4] = calculatingSboxOutput(5, x[3]) ^ calculatingSboxOutput(6, x[2]) ^ calculatingSboxOutput(7, x[
        12]) \
                           ^ calculatingSboxOutput(8, x[13]) ^ calculatingSboxOutput(5, x[8])

    # S5[x1] ^ S6[x0] ^ S7[xE] ^ S8[xF] ^ S6[xD]
    keysArray[i * 8 + 5] = calculatingSboxOutput(5, x[1]) ^ calculatingSboxOutput(6, x[0]) ^ calculatingSboxOutput(7, x[
        14]) \
                           ^ calculatingSboxOutput(8, x[15]) ^ calculatingSboxOutput(6, x[13])

    #       S5[x7] ^ S6[x6] ^ S7[x8] ^ S8[x9] ^ S7[x3]
    keysArray[i * 8 + 6] = calculatingSboxOutput(5, x[7]) ^ calculatingSboxOutput(6, x[6]) ^ calculatingSboxOutput(7,
                                                                                                                   x[8]) \
                           ^ calculatingSboxOutput(8, x[9]) ^ calculatingSboxOutput(7, x[3])

    #   S5[x5] ^ S6[x4] ^ S7[xA] ^ S8[xB] ^ S8[x7]
    keysArray[i * 8 + 7] = calculatingSboxOutput(5, x[5]) ^ calculatingSboxOutput(6, x[4]) ^ calculatingSboxOutput(7, x[
        10]) \
                           ^ calculatingSboxOutput(8, x[11]) ^ calculatingSboxOutput(8, x[7])


def calculateKeys3(keysArray, z1, i):
    #                                           S5[z3] ^ S6[z2] ^ S7[zC] ^ S8[zD] ^ S5[z9]
    keysArray[i * 8 + 0] = calculatingSboxOutput(5, z1[3]) ^ calculatingSboxOutput(6, z1[2]) ^ calculatingSboxOutput(7,
                                                                                                                     z1[
                                                                                                                         12]) \
                           ^ calculatingSboxOutput(8, z1[13]) ^ calculatingSboxOutput(5, z1[9])

    #                                           S5[z1] ^ S6[z0] ^ S7[zE] ^ S8[zF] ^ S6[zC]
    keysArray[i * 8 + 1] = calculatingSboxOutput(5, z1[1]) ^ calculatingSboxOutput(6, z1[0]) ^ calculatingSboxOutput(7,
                                                                                                                     z1[
                                                                                                                         14]) \
                           ^ calculatingSboxOutput(8, z1[15]) ^ calculatingSboxOutput(6, z1[12])

    #                                           S5[z7] ^ S6[z6] ^ S7[z8] ^ S8[z9] ^ S7[z2]
    keysArray[i * 8 + 2] = calculatingSboxOutput(5, z1[7]) ^ calculatingSboxOutput(6, z1[6]) ^ calculatingSboxOutput(7,
                                                                                                                     z1[
                                                                                                                         8]) \
                           ^ calculatingSboxOutput(8, z1[9]) ^ calculatingSboxOutput(7, z1[2])

    #                                           S5[z5] ^ S6[z4] ^ S7[zA] ^ S8[zB] ^ S8[z6]
    keysArray[i * 8 + 3] = calculatingSboxOutput(5, z1[5]) ^ calculatingSboxOutput(6, z1[4]) ^ calculatingSboxOutput(7,
                                                                                                                     z1[
                                                                                                                         10]) \
                           ^ calculatingSboxOutput(8, z1[11]) ^ calculatingSboxOutput(8, z1[6])


def calculateKeys4(keysArray, x, i):
    #                                           S5[x8] ^ S6[x9] ^ S7[x7] ^ S8[x6] ^ S5[x3]
    keysArray[i * 8 + 4] = calculatingSboxOutput(5, x[8]) ^ calculatingSboxOutput(6, x[9]) ^ calculatingSboxOutput(7,
                                                                                                                   x[7]) \
                           ^ calculatingSboxOutput(8, x[6]) ^ calculatingSboxOutput(5, x[3])

    #                                           S5[xA] ^ S6[xB] ^ S7[x5] ^ S8[x4] ^ S6[x7]
    keysArray[i * 8 + 5] = calculatingSboxOutput(5, x[10]) ^ calculatingSboxOutput(6, x[11]) ^ calculatingSboxOutput(7,
                                                                                                                     x[
                                                                                                                         5]) \
                           ^ calculatingSboxOutput(8, x[4]) ^ calculatingSboxOutput(6, x[7])

    #                                           S5[xC] ^ S6[xD] ^ S7[x3] ^ S8[x2] ^ S7[x8]
    keysArray[i * 8 + 6] = calculatingSboxOutput(5, x[12]) ^ calculatingSboxOutput(6, x[13]) ^ calculatingSboxOutput(7,
                                                                                                                     x[
                                                                                                                         3]) \
                           ^ calculatingSboxOutput(8, x[2]) ^ calculatingSboxOutput(7, x[8])

    #                                            S5[xE] ^ S6[xF] ^ S7[x1] ^ S8[x0] ^ S8[xD]
    keysArray[i * 8 + 7] = calculatingSboxOutput(5, x[14]) ^ calculatingSboxOutput(6, x[15]) ^ calculatingSboxOutput(7,
                                                                                                                     x[
                                                                                                                         1]) \
                           ^ calculatingSboxOutput(8, x[0]) ^ calculatingSboxOutput(8, x[13])


def generateMaskingAndRotationKeys(keysArray):
    Km = [None] * 16
    Kr = [None] * 16
    for i in range(16):
        Km[i] = keysArray[i]
        Kr[i] = keysArray[16 + i][27:32]

    return Km, Kr
