from lib.myFunc import intArray
import time

inputArray = []


def run(part, path):
    global inputArray
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = intArray(inputFile.split('\n'))

        # inputArray.remove("")

    lastJolt = 0
    differenceCount = [0, 0, 0, 0]  # 1 jolt =[1], 2 jolt =[2] ...
    usedAdapters = []

    deviceRating = max(inputArray) + 3

    inputArray.append(deviceRating)
    inputArray.append(0)
    inputArray = sorted(inputArray)
    print(inputArray)
    if part == 1:
        for pos in range(len(inputArray)):
            if lastJolt < inputArray[pos] < lastJolt + 4:
                print("last", lastJolt, "current:", inputArray[pos])
                print("difference:", inputArray[pos] - lastJolt)
                differenceCount[inputArray[pos] - lastJolt] += 1
                usedAdapters.append(inputArray[pos])
                lastJolt = inputArray[pos]

        differenceCount[deviceRating - lastJolt] += 1

        print(deviceRating)
        print(inputArray)
        print(differenceCount)
        solution = differenceCount[1] * differenceCount[3]
        print("Solution:", solution)

    if part == 2:
        startTime = time.time()

        print("Solution:", recursiveCheck(0))
        print("calculating Time: ", (time.time() - startTime))


checkedArray = []


def recursiveCheck_old(list):
    count = 0
    last = -1
    if list in checkedArray:
        return 0

    for pos in range(len(list)):
        if not last < list[pos] < last + 4:
            return 0
        last = list[pos]
    count += 1
    print(list)

    for pos in range(1, len(list) - 2):
        if list[pos - 1] < list[pos + 1] < list[pos + 2] + 4:
            listCopy = list.copy()
            listCopy.pop(pos)
            count += recursiveCheck_old(listCopy)
    print(count)
    checkedArray.append(list)
    return count


DP = {}


def recursiveCheck(i):
    if i == len(inputArray) - 1:
        return 1
    if i in DP:
        return DP[i]
    count = 0
    for j in range(i + 1, len(inputArray)):
        if inputArray[j] - inputArray[i] <= 3:
            count += recursiveCheck(j)
    DP[i] = count
    return count
