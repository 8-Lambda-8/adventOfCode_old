import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        del inputFile
    startTime = time.time()
    if part == 1:
        print("Solution:", "noSolution")

    if part == 2:
        print("Solution:", "noSolution")

    print("calculating Time: ", (time.time() - startTime))
