import time


def fuelConsumption(offset):
    fuel = 0
    for f in range(offset):
        fuel += 1 + f
    return fuel


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split(',')
        # inputArray.remove("")
        inputArray = list(map(int, inputArray))  # strings to int
        del inputFile
    startTime = time.perf_counter()

    if part == 1:
        fuelForX = [0] * max(inputArray)

        for X in range(len(fuelForX)):
            for crab in inputArray:
                if crab > X:
                    fuelForX[X] += abs(crab - X)
                else:
                    fuelForX[X] += (X - crab)

        print("Solution Part 1:", min(fuelForX))

    if part == 2:
        fuelForX = [0] * max(inputArray)

        for X in range(len(fuelForX)):
            for crab in inputArray:
                if crab > X:
                    fuelForX[X] += fuelConsumption(crab - X)
                else:
                    fuelForX[X] += fuelConsumption(X - crab)
        print("Solution Part 2:", min(fuelForX))

    print("calculating Time: ", (time.perf_counter() - startTime) * 1000, "ms")


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
