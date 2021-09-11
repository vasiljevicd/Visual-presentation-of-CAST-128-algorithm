from bitarray.util import *

from core.sboxes import calculatingSboxOutput


def roundsForAlgorithm(L, R, Km, Kr, numberOfRounds, encryptionOrDecryption):
    I = [None] * numberOfRounds
    f = [None] * numberOfRounds
    if encryptionOrDecryption:
        for i in range(numberOfRounds):
            I1 = [None] * 4
            # 1, 4, 7, 10, 13, and 16
            if i == 0 or i == 3 or i == 6 or i == 9 or i == 12 or i == 15:
                sumBitArray = additionModulo2exp32(Km[i], R[i])
                I[i] = circularLeftRotation(sumBitArray, Kr[i])
                I1 = divideITo4Parts(I[i])
                f[i] = function1(I1)
            # Rounds 2, 5, 8, 11, and 14 use f function Type 2.
            elif i == 1 or i == 4 or i == 7 or i == 10 or i == 13:
                xorResult = Km[i] ^ R[i]
                I[i] = circularLeftRotation(xorResult, Kr[i])
                I1 = divideITo4Parts(I[i])
                f[i] = function2(I1)
                # Rounds 3, 6, 9, 12, and 15 use f function Type 3.
            elif i == 2 or i == 5 or i == 8 or i == 11 or i == 14:
                subResult = subtractionModulo2exp32(Km[i], R[i])
                I[i] = circularLeftRotation(subResult, Kr[i])
                I1 = divideITo4Parts(I[i])
                f[i] = function3(I1)

            L[i + 1] = R[i]
            R[i + 1] = L[i] ^ f[i]
    else:
        for i in range(numberOfRounds-1, -1, -1):
            I1 = [None] * 4
            # 1, 4, 7, 10, 13, and 16
            if i == 0 or i == 3 or i == 6 or i == 9 or i == 12 or i == 15:
                sumBitArray = additionModulo2exp32(Km[i], R[i+1])
                I[i] = circularLeftRotation(sumBitArray, Kr[i])
                I1 = divideITo4Parts(I[i])
                f[i] = function1(I1)
            # Rounds 2, 5, 8, 11, and 14 use f function Type 2.
            elif i == 1 or i == 4 or i == 7 or i == 10 or i == 13:
                xorResult = Km[i] ^ R[i+1]
                I[i] = circularLeftRotation(xorResult, Kr[i])
                I1 = divideITo4Parts(I[i])
                f[i] = function2(I1)
                # Rounds 3, 6, 9, 12, and 15 use f function Type 3.
            elif i == 2 or i == 5 or i == 8 or i == 11 or i == 14:
                subResult = subtractionModulo2exp32(Km[i], R[i+1])
                I[i] = circularLeftRotation(subResult, Kr[i])
                I1 = divideITo4Parts(I[i])
                f[i] = function3(I1)

            L[i] = R[i+1]
            R[i] = L[i+1] ^ f[i]

    return L, R, Km, Kr, I, f


def divideITo4Parts(I):
    x = []
    for i in range(4):
        x.append(I[i * 8:(i + 1) * 8])
    print(x)
    return x


def circularLeftRotation(moduleResult, Kr):
    x = ba2int(Kr)
    print('x', x)
    temp = moduleResult[0:x]
    moduleResult <<= x
    moduleResult[32 - x:32] = temp
    print(moduleResult)
    return moduleResult


def additionModulo2exp32(term1, term2):
    sumInt = (ba2int(term1) + ba2int(term2)) % (2 ** 32)
    sumBitArray = int2ba(sumInt, 32)
    return sumBitArray


def subtractionModulo2exp32(term1, term2):
    sumInt = (ba2int(term1) - ba2int(term2)) % (2 ** 32)
    sumBitArray = int2ba(sumInt, 32)
    return sumBitArray


def function1(I):
    # f = ((S1[Ia] ^ S2[Ib]) - S3[Ic]) + S4[Id]
    xorResult = calculatingSboxOutput(1, I[0]) ^ calculatingSboxOutput(2, I[1])
    subResult = subtractionModulo2exp32(xorResult, calculatingSboxOutput(3, I[2]))
    sumResult = additionModulo2exp32(subResult, calculatingSboxOutput(4, I[3]))
    return sumResult


def function2(I):
    # f = ((S1[Ia] - S2[Ib]) + S3[Ic]) ^ S4[Id]
    subResult = subtractionModulo2exp32(calculatingSboxOutput(1, I[0]), calculatingSboxOutput(2, I[1]))
    sumResult = additionModulo2exp32(subResult, calculatingSboxOutput(3, I[2]))
    xorResult = sumResult ^ calculatingSboxOutput(4, I[3])
    return xorResult


def function3(I):
    # f = ((S1[Ia] + S2[Ib]) ^ S3[Ic]) - S4[Id]
    sumResult = additionModulo2exp32(calculatingSboxOutput(1, I[0]), calculatingSboxOutput(2, I[1]))
    xorResult = sumResult ^ calculatingSboxOutput(3, I[2])
    subResult = subtractionModulo2exp32(xorResult, calculatingSboxOutput(4, I[3]))
    return subResult
