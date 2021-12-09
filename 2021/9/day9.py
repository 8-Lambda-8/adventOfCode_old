import time

inputArray = []


def checkIfAnyRemaining():
    for line in inputArray:
        for char in line:
            if char not in ["X", "O"]:
                return True
    return False


def getBasin(x, y):
    global inputArray
    inputArray[y] = inputArray[y][:x] + 'O' + inputArray[y][x + 1:]
    size = 1
    for loc in adjacentLocations(x, y, inputArray):
        if inputArray[loc[2]][loc[1]] not in ["X", "O"]:
            size += getBasin(loc[1], loc[2])
    return size


def adjacentLocations(x, y, array):
    neighbours = []

    if x > 0:
        neighbours.append((array[y][x - 1], x - 1, y))
    if y > 0:
        neighbours.append((array[y - 1][x], x, y - 1))
    if x < len(array[0]) - 1:
        neighbours.append((array[y][x + 1], x + 1, y))
    if y < len(array) - 1:
        neighbours.append((array[y + 1][x], x, y + 1))
    return neighbours


def run(part, path):
    global inputArray
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        inputArray.remove("")
        # inputArray = list(map(int, inputArray)) # strings to int
        del inputFile
    startTime = time.perf_counter()
    if part == 1:
        riskLevel = 0
        for y in range(len(inputArray)):
            for x in range(len(inputArray[0])):
                if all(inputArray[y][x] < loc[0] for loc in adjacentLocations(x, y, inputArray)):
                    print("riskyPoint:", x, y, inputArray[y][x])
                    riskLevel += 1 + int(inputArray[y][x])

        print("Solution Part 1:", riskLevel)

    if part == 2:
        basins = []
        for y in range(len(inputArray)):
            inputArray[y] = inputArray[y].replace("9", "X")
            print(inputArray[y])

        # print(getBasin(0, 0))
        # print(inputArray)
        while checkIfAnyRemaining():
            print("\n")
            for y in range(len(inputArray)):
                print(inputArray[y])
            for y in range(len(inputArray)):
                for x, val in enumerate(inputArray[0]):
                    if inputArray[y][x] not in ["X", "O"]:
                        basins.append(getBasin(x, y))
                        break
                else:
                    continue
                break

        print("\n")
        for y in range(len(inputArray)):
            print(inputArray[y])
        print(basins)
        solution = max(basins)
        basins.remove(max(basins))
        solution *= max(basins)
        basins.remove(max(basins))
        solution *= max(basins)
        basins.remove(max(basins))
        print("Solution Part 2:", solution)

    print("calculating Time: {:10.3f} ms ".format((time.perf_counter() - startTime) * 1000))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
