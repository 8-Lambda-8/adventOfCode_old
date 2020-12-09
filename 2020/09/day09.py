from lib.myFunc import intArray


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = intArray(inputFile.split('\n'))
        # inputArray.remove("")

    if part == 1:
        preambleLength = 25
        solution = 0
        for i in range(preambleLength, len(inputArray)):

            print("\n", i, ": ", inputArray[i])
            previousNumbers = inputArray[i - preambleLength:i]
            print(previousNumbers)
            for x in previousNumbers:
                for y in previousNumbers:

                    if (x + y) == inputArray[i]:
                        print("found values: ", x, y, "")
                        break
                else:
                    continue
                break
            else:
                solution = inputArray[i]
                print("values not found: ", inputArray[i], )
                break

        print("Solution:", solution)

    solution1 = 20874512
    # solution1 = 127 //for test
    if part == 2:

        solution = 0
        for i in range(len(inputArray)):
            j = 0
            contiguousNumberSum = 0
            print("\nfirst in try: i=", i, inputArray[i])
            while contiguousNumberSum < solution1 and i + j < len(inputArray):
                contiguousNumberSum += inputArray[i + j]
                # print(inputArray[i + j])
                j += 1
            print("j=", j)
            # print("higher or equal")

            arrayOfContiguousNumbers = inputArray[i:i + j]
            print(arrayOfContiguousNumbers)
            arrayOfContiguousNumbers.sort()

            if contiguousNumberSum == solution1:
                solution = arrayOfContiguousNumbers[0] + arrayOfContiguousNumbers[-1]
                break
        print("Solution:", solution)
