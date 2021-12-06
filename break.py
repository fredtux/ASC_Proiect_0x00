# Sursa: https://math.stackexchange.com/questions/28955/how-to-break-xor-cipher-with-repeating-key al 2-lea raspuns

from collections import Counter


def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


with open("output", "rb") as f:
    binput = bytearray(f.read())
    for k in range(10, 16):
        key = []
        for j in range(k):
            highest = []
            for i in range(j,len(binput), k):
                highest.append(binput[i] ^ 0x20)
            key.append(chr(most_frequent(highest)))

        isValid = True

        for i in key:
            if not i.isalnum():
                isValid = False
                break
        if isValid:
            print("".join(key))
