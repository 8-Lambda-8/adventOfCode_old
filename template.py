import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        del inputFile
    startTime = time.perf_counter()
    if part == 1:
        print("Solution Part 1:", "noSolution")

    if part == 2:
        print("Solution Part 2:", "noSolution")

    print("calculating Time: ", (time.perf_counter() - startTime))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
