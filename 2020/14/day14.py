import time
from itertools import product

from lib.myFunc import replaceCharAt


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
    startTime = time.time()

    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    address = 0
    val = 0

    # mem = pow(2, 16)*[0]
    mem = {}

    if part == 1:

        for line in inputArray:
            if line.startswith("mask"):
                mask = line.split(" ")[-1]
            elif line.startswith("mem"):
                address = int(line[4:line.index("]")])
                val = int(line.split(" ")[-1])

                print(mask, address, val)
                valString = format(val, '#038b')[2:]
                for pos in range(len(valString)):
                    if not mask[pos] == "X":
                        valString = replaceCharAt(valString, pos, mask[pos])

                val = int(valString, 2)
                print(val)
                mem[address] = int(valString, 2)

        count = 0
        for address in mem:
            count += mem[address]
        print("Solution:", count)

    if part == 2:
        for line in inputArray:
            if line.startswith("mask"):
                mask = line.split(" ")[-1]
            elif line.startswith("mem"):
                address = int(line[4:line.index("]")])
                val = int(line.split(" ")[-1])

                print(mask, address, val)
                addressString = format(address, '#038b')[2:]
                for pos in range(len(addressString)):
                    if not mask[pos] == "0":
                        addressString = replaceCharAt(addressString, pos, mask[pos])

                addressString_format = addressString.replace('X', '{}')
                for i in product('01', repeat=addressString.count('X')):
                    address = int(addressString_format.format(*i), 2)
                    mem[address] = val

        count = 0
        for address in mem:
            count += mem[address]
        print("Solution:", count)

    print("calculating Time: ", (time.time() - startTime))
