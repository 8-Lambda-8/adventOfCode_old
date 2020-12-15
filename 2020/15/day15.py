import time

from lib.myFunc import intArray, lastIndexOf


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        numbers = intArray(inputFile.split(','))
        # inputArray.remove("")
    startTime = time.time()

    if part == 1:
        for i in range(len(numbers), 2020):
            print(i, ":", "LastSpoken: ", numbers[i - 1])
            # print("countLastSpoken", numbers.count(numbers[i - 1]))
            if numbers.count(numbers[i - 1]) == 1:
                numbers.append(0)
            else:
                # print("lastIndexOf", numbers[i-1], ":", lastIndexOf(numbers, numbers[i-1]))

                lastIndex = lastIndexOf(numbers, numbers[i - 1])
                lastIndexBefore = lastIndexOf(numbers[:lastIndex], numbers[i - 1])
                numbers.append(lastIndex - lastIndexBefore)
            print(numbers)

        print("Solution:", numbers[-1])

    if part == 2:
        # convert To Dict
        numbersDict = {}
        lastNumber = numbers[-1]
        for pos, val in enumerate(numbers):
            numbersDict[val] = [pos, None]

        print(numbersDict)

        del numbers

        for i in range(len(numbersDict), 30000000):
            print(i)
            if numbersDict[lastNumber][1] is None:
                lastNumber = 0
                numbersDict[lastNumber] = [i, numbersDict[lastNumber][0]]
            else:
                lastNumber = numbersDict[lastNumber][0] - numbersDict[lastNumber][1]
                if lastNumber not in numbersDict:
                    numbersDict[lastNumber] = [i, None]
                else:
                    numbersDict[lastNumber] = [i, numbersDict[lastNumber][0]]

        # print(numbersDict, len(numbersDict))
        print("Solution:", lastNumber)

    print("calculating Time: ", (time.time() - startTime))


