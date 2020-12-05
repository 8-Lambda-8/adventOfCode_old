def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split('\n')
        inputArray.remove("")

    highestSeatId = 0



    if part == 1:
        for line in inputArray:
            low = 0
            high = 127

            for i in range(7):
                low, high = binarySearch(line[i], low, high)

            seatId = low * 8

            low = 0
            high = 7
            for i in range(7,10):
                low, high = binarySearch(line[i], low, high)

            seatId += low

            if seatId > highestSeatId:
                highestSeatId = seatId

        print("Solution:", highestSeatId)

    if part == 2:
        existingSeatIds = []

        for line in inputArray:
            low = 0
            high = 127

            for i in range(7):
                low, high = binarySearch(line[i], low, high)

            seatId = low * 8

            low = 0
            high = 7
            for i in range(7, 10):
                low, high = binarySearch(line[i], low, high)

            seatId += low

            print(seatId)

            existingSeatIds.append(seatId)
            existingSeatIds.sort()

        print(existingSeatIds)
        print("")
        mySeatId = 0

        for i in range(1, len(existingSeatIds)-1):
            print(existingSeatIds[i-1], existingSeatIds[i])
            if existingSeatIds[i-1]+1 != existingSeatIds[i]:
                mySeatId = existingSeatIds[i]-1
                break

        print("Solution:", mySeatId)


def binarySearch(char, low, high):
    mid = (low + high) // 2
    # print(mid)
    if char in ["F", "L"]:
        high = mid
    elif char in ["B", "R"]:
        low = mid+1
    return low, high

