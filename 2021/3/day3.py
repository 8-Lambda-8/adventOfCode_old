import time


def mostCommon(lst, i):
    x = 0
    for line in lst:
        if line[i] == "1":
            x += 1
    if x >= len(lst) / 2:
        return "1"
    else:
        return "0"


def leastCommon(lst, i):
    return '0' if mostCommon(lst, i) == '1' else '1'


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        inputArray.remove("")
        # inputArray = list(map(int, inputArray)) //strings to int
        del inputFile
    startTime = time.perf_counter()

    g = ""
    e = ""
    lineBits = [0] * len(inputArray[0])
    if part == 1:
        for line in inputArray:
            for i, char in enumerate(line):
                if char == "1":
                    lineBits[i] += 1
        for bits in lineBits:
            if bits > len(inputArray) / 2:
                g += "1"
            else:
                g += "0"

        for bit in g:
            if bit == "1":
                e += "0"
            else:
                e += "1"
        print("g=", g)
        print("e=", e)
        print("Solution Part 1: ", int(g, 2) * int(e, 2))

    if part == 2:
        inputOxy = list(inputArray)
        inputCo2 = list(inputArray)

        for i in range(len(inputArray[0])):
            if len(inputOxy) > 1:
                inputOxy = list(filter(lambda x: x[i] == mostCommon(inputOxy, i), inputOxy))
            if len(inputCo2) > 1:
                inputCo2 = list(filter(lambda x: x[i] == leastCommon(inputCo2, i), inputCo2))

            # print("O", inputOxy)
            # print("C", inputCo2)

        print("Solution Part 2:", int(inputOxy[0], 2) * int(inputCo2[0], 2))

    print("calculating Time: ", (time.perf_counter() - startTime))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
