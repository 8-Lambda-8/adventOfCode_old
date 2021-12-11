import time

inputArray = []
flashedOctopus = []
flashes = 0


def checkIfFlashing():
    global inputArray
    return any(any(octopus > 9 for octopus in line) for line in inputArray)


def checkIfAllFlashing():
    global inputArray, flashedOctopus
    return all(all(octopus for octopus in line) for line in flashedOctopus)


def flash(x, y):
    global flashes
    inputArray[y][x] = 0
    if not flashedOctopus[y][x]:
        flashedOctopus[y][x] = True
        flashes += 1
        for y_ in range(max(0, y - 1), min(len(inputArray), y + 2)):
            for x_ in range(max(0, x - 1), min(len(inputArray[0]), x + 2)):
                if not (x_ == x and y_ == y):
                    inputArray[y_][x_] += 1


def run(part, path):
    global inputArray, flashedOctopus, flashes
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = [list(map(int, [char for char in line])) for line in inputFile.split('\n')]
        del inputFile
    startTime = time.perf_counter()

    print(inputArray)

    if part == 1:
        for i in range(100):
            print(i)
            flashedOctopus = [[False] * len(inputArray[0]) for i in range(len(inputArray))]
            for y, line in enumerate(inputArray):
                for x, octopus in enumerate(line):
                    inputArray[y][x] += 1
            while checkIfFlashing():
                for y, line in enumerate(inputArray):
                    for x, octopus in enumerate(line):
                        if octopus > 9:
                            flash(x, y)
                            break
                    else:
                        continue
                    break
            for y, line in enumerate(inputArray):
                for x, octopus in enumerate(line):
                    if flashedOctopus[y][x]:
                        inputArray[y][x] = 0

        print("Solution Part 1:", flashes)

    if part == 2:
        i = 0
        flashedOctopus = [[False] * len(inputArray[0]) for i in range(len(inputArray))]
        while not checkIfAllFlashing():
            print(i)
            i += 1
            flashedOctopus = [[False] * len(inputArray[0]) for i in range(len(inputArray))]
            for y, line in enumerate(inputArray):
                for x, octopus in enumerate(line):
                    inputArray[y][x] += 1
            while checkIfFlashing():
                for y, line in enumerate(inputArray):
                    for x, octopus in enumerate(line):
                        if octopus > 9:
                            flash(x, y)
                            break
                    else:
                        continue
                    break
            for y, line in enumerate(inputArray):
                for x, octopus in enumerate(line):
                    if flashedOctopus[y][x]:
                        inputArray[y][x] = 0

        print("Solution Part 2:", i)

    print("calculating Time: {:10.3f} ms ".format((time.perf_counter() - startTime) * 1000))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
