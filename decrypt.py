from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser(description="Decrypts a file using xor")
    parser.add_argument("input", metavar="input_file", type=str, help="File that will be decrypted")
    parser.add_argument("key", metavar="key", type=str, help="XOR key")
    parser.add_argument("output", metavar="output", type=str, help="File containing the decrypted text")

    args = parser.parse_args()
    return args


def get_input_bytearray(input_file):
    with open(input_file, "rb") as file:
        res = bytearray(file.read())
        return res


def output_file(output_file, bstring):
    with open(output_file, "wb") as file:
        file.write(bstring)


def decrypt(key, binput):
    rez = []
    i = 0
    kl = len(key)
    for index, value in enumerate(binput):
        rez.append(value ^ key[i])
        i = (i + 1) % kl  # Rotate through key
    return rez


# Get arguments
args = get_arguments()

# Get input and make it a bytearray
binput = get_input_bytearray(args.input)

# Make key a bytearray
key = bytearray(args.key, encoding="UTF-8")
if 10 > len(key) or len(key) > 15:
    print("Key must be between 10 and 15 characters!!!")
    exit(0)

# Decrypt
output = decrypt(key, binput)
output_file(args.output, bytearray(output))
