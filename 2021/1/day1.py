import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        inputArray.remove("")
        inputArray = list(map(int, inputArray))
        del inputFile

    startTime = time.perf_counter()
    if part == 1:
        increased = 0
        for i, line in enumerate(inputArray):
            if i != 0 and line > inputArray[i - 1]:
                increased += 1

        print("Solution Part 1:", increased)

    if part == 2:
        increased = 0
        for i, line in enumerate(inputArray):
            if i > 2 and (line+inputArray[i-1]+inputArray[i-2])>(inputArray[i-1]+inputArray[i-2]+inputArray[i-3]):
                increased += 1
        print("Solution Part 2:", increased)

    print("calculating Time: ", (time.perf_counter() - startTime))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
