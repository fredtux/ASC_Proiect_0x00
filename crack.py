from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser(description="Encrypts a file using xor")
    #parser.add_argument("key", metavar="key", type=str, help="XOR key")
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
    k =[]
    for char in binput:
        k.append(chr(binput[i] ^ boutput[i]))
        i += 1

    return k


# Get arguments
args = get_arguments()

# Get input and make it a bytearray
binput = get_input_bytearray(args.input)

# Get output
boutput = get_input_bytearray(args.output)

# Crack the key
key = crack(binput, boutput)

for i in range(len(key)):
    print(key[i], end = '')

