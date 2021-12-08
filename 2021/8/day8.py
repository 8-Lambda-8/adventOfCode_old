import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        # inputArray = list(map(int, inputArray)) # strings to int
        del inputFile
    startTime = time.perf_counter()

    if part == 1:
        solution = 0
        for line in inputArray:
            input_, output = line.split(" | ")
            print(output)
            for digit in output.split(" "):
                digitLen = len(digit)
                print(digitLen)
                if digitLen == 2 or digitLen == 3 or digitLen == 4 or digitLen == 7:
                    solution += 1

        print("Solution Part 1:", solution)

    if part == 2:
        solution = 0
        for line in inputArray:
            input_, output = line.split(" | ")
            digitMap = {}
            reverseDigitMap = {}
            segmentCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
            print(line)

            for digit in input_.split(" "):
                digit = "".join(sorted(digit))
                digitLen = len(digit)
                for x in digit:
                    segmentCount[x] += 1

                if digitLen == 2:  # One
                    digitMap[digit] = 1
                    reverseDigitMap[1] = digit
                if digitLen == 3:  # seven
                    digitMap[digit] = 7
                    reverseDigitMap[7] = digit
                if digitLen == 4:  # four
                    digitMap[digit] = 4
                    reverseDigitMap[4] = digit
                if digitLen == 7:  # eight
                    digitMap[digit] = 8
                    reverseDigitMap[8] = digit

                if digitLen == 6:
                    digitMap[digit] = [6, 9, 0]
                if digitLen == 5:
                    digitMap[digit] = [2, 3, 5]

            # solve the remaining stuff:
            # 6, 9, 0:
            in6and2 = reverseDigitMap[8]
            for x in reverseDigitMap[4]:
                in6and2 = in6and2.replace(x, "")

            # check 6 digits
            for digit in [key for key, value in digitMap.items() if value == [6, 9, 0]]:
                digit = "".join(sorted(digit))

                if all(char in digit for char in in6and2):
                    if all(char in digit for char in reverseDigitMap[1]):  # zero
                        digitMap[digit] = 0
                        reverseDigitMap[0] = digit
                    else:  # six
                        digitMap[digit] = 6
                        reverseDigitMap[6] = digit
                else:
                    digitMap[digit] = 9
                    reverseDigitMap[9] = digit

            # 2, 3, 3
            # check 5 digits
            for digit in [key for key, value in digitMap.items() if value == [2, 3, 5]]:
                digit = "".join(sorted(digit))
                if all(char in digit for char in in6and2):  # two
                    digitMap[digit] = 2
                    reverseDigitMap[2] = digit
                elif all(char in digit for char in reverseDigitMap[1]):  # three
                    digitMap[digit] = 3
                    reverseDigitMap[3] = digit
                else:  # five
                    digitMap[digit] = 5
                    reverseDigitMap[5] = digit

            outputNumber = ""
            for digit in output.split(" "):
                digit = "".join(sorted(digit))
                outputNumber += str(digitMap[digit])

            print(outputNumber)

            solution += int(outputNumber)

        print("Solution Part 2:", solution)

    print("calculating Time: {:10.3f} ms ".format((time.perf_counter() - startTime) * 1000))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
