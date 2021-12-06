import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split(',')
        inputArray = list(map(int, inputArray))
        del inputFile
    startTime = time.perf_counter()

    if part == 1:
        newFish = 0
        for day in range(80):
            print(day, len(inputArray))
            # print(inputArray)

            for i, fish in enumerate(inputArray):
                if fish < 1:
                    inputArray[i] = 6
                    newFish += 1
                else:
                    inputArray[i] -= 1

            for i in range(newFish):
                inputArray.append(8)
            newFish = 0
        print("Solution Part 1:", len(inputArray))

    if part == 2:
        fishMap = {i: 0 for i in range(9)}
        for fish in inputArray:
            fishMap[fish] += 1

        for days in range(256 + 1):
            print(fishMap)
            zeroDay = fishMap[0]
            for i in range(8):
                fishMap[i] = fishMap[i + 1]
            fishMap[6] += zeroDay
            fishMap[8] = zeroDay

        solution = 0
        for i in range(8):
            solution += fishMap[i]

        print("Solution Part 2:", solution)

    print("calculating Time: ", (time.perf_counter() - startTime) * 1000, "ms")


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
