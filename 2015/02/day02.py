from lib import myFunc


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split('\n')
        inputArray = [myFunc.intArray(line.split('x')) for line in inputArray]

    if part == 1:
        orderArea = 0
        for line in inputArray:
            line.sort()
            [l, w, h] = line
            orderArea += area(l, w, h)
            orderArea += areaSmallestSide(l, w, h)

        print("Solution:", orderArea)

    if part == 2:
        orderLength = 0
        for line in inputArray:
            line.sort()
            [l, w, h] = line
            orderLength += 2 * (l + w)
            orderLength += l * w * h

        print("Solution:", orderLength)


def area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


def areaSmallestSide(l, w, h):
    lengthList = [l, w, h]
    lengthList.sort()
    return lengthList[0] * lengthList[1]
