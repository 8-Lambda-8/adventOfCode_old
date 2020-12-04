def run(part, path):
    import time

    with open(path, 'r') as file:
        inputArray = file.read().split('\n')

    # convert to int
    inputArray = list(map(int, inputArray))

    compareValue = 2020
    startTime = time.time()
    # Part One
    if part == 1:
        for x in inputArray:
            for y in inputArray:
                print(x, "+", y, "=", x + y)
                if (x + y) == compareValue:
                    print("values are:", x, " ", y)
                    print("solution is: ", x * y)
                    break
            else:
                continue
            break

    # Part Two
    if part == 2:
        for x in inputArray:
            for y in inputArray:
                # if x == y:
                #     continue
                for z in inputArray:
                    # if x == z or y == z:
                    #     continue
                    # print(x, "+", y, "+", z, "=", x + y +z)
                    if ((x + y) + z) == compareValue:
                        print("values are:", x, " ", y, " ", z)
                        print("solution is: ", x * y * z)

                        print("calculating Time: ", (time.time() - startTime))
                        break
                else:
                    continue
                break
            else:
                continue
            break
