def intArray(stringArray):
    for pos, num in enumerate(stringArray):
        # print(num)
        stringArray[pos] = int(num)
    return stringArray


def replaceCharAt(string, index, char):
    return string[0:index] + char + string[index + 1:]


def compareTuple(minTup, maxTup, Tup):
    return minTup[0] < Tup[0] < maxTup[0] and minTup[1] < Tup[1] < maxTup[1]


def lastIndexOf(searchList, val):
    return len(searchList) - 1 - searchList[::-1].index(val)
