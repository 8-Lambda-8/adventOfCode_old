from lib.myFunc import intArray

lightArray = 10 * [10 * [False]]


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split('\n')
        inputArray.remove("")

    inputArray = ["turn on 0,0 through 9,9",
                  "turn off 2,2 through 4,4"]

    lightCount = 0
    if part == 1:
        for line in inputArray:
            line = line.split(" ")
            # print(line)
            if line[0] == "turn":
                setLights(intArray(line[2].split(",")), intArray(line[-1].split(",")), line[1] == "on")
            elif line[0] == "toggle":
                toggleLights(intArray(line[1].split(",")), intArray(line[-1].split(",")))

        [print(intArray(y)) for y in lightArray]

        for y in lightArray:
            for x in y:
                if x:
                    lightCount += 1

        print("Solution:", lightCount)

    if part == 2:
        print("Solution:", "noSolution")


def setLights(start, end, state):
    for y in range(start[1], end[1] + 1):
        for x in range(start[0], end[0] + 1):
            # print("from", lightArray[y][x])
            lightArray[y][x] = state
            # print("to", lightArray[y][x])


def toggleLights(start, end):
    for y in range(start[1], end[1] + 1):
        for x in range(start[0], end[0] + 1):
            # print("from", lightArray[y][x])
            lightArray[y][x] = not lightArray[x][y]
            # print("to", lightArray[y][x])
