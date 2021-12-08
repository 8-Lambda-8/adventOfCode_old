import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        # inputArray = list(map(int, inputArray)) # strings to int
        del inputFile
    startTime = time.perf_counter()
    if part == 1:
        print("Solution Part 1:", "noSolution")

    if part == 2:
        print("Solution Part 2:", "noSolution")

    print("calculating Time: {:10.3f} ms ".format((time.perf_counter() - startTime) * 1000))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
