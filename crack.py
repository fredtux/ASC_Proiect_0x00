from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser(description="Encrypts a file using xor")
    parser.add_argument("input", metavar="input_file", type=str, help="File that will be encrypted")
    parser.add_argument("output", metavar="output", type=str, help="File containing the encrypted text")

    args = parser.parse_args()

    return args


def get_input_bytearray(input_file):
    with open(input_file, "rb") as file:
        res = bytearray(file.read())

        return res


def crack(binput, boutput):
    i = 0
    k = []
    for char in binput:
        k.append(chr(binput[i] ^ boutput[i]))
        i += 1

    return k


def encrypt(key, binput):
    res = []

    i = 0
    kl = len(key)
    for _, value in enumerate(binput):
        res.append(value ^ key[i])

        i = (i + 1) % kl  # Rotate through key

    return res


def bisEqual(b1, b2):
    if len(b1) != len(b2):
        return False

    for i in range(len(b1)):
        if b1[i] != b2[i]:
            return False

    return True


# Get arguments
args = get_arguments()

# Get input and make it a bytearray
binput = get_input_bytearray(args.input)

# Get output
boutput = get_input_bytearray(args.output)

# Crack the key
rkey = crack(binput, boutput)  # Returned key
key = ""

for i in range(10, 16):
    pkey = "".join(rkey[:i + 1])  # Possible key
    bkey = bytearray(pkey, encoding="UTF-8")  # Byte-array key
    if bisEqual(encrypt(bkey, binput), boutput):
        key = pkey
        break
else:
    key = []
    for i in range(len(rkey)):
        key.append(rkey[i])
    key = "".join(key)

print(key)
