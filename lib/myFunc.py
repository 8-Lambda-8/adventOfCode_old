def intArray(stringArray):
    for pos, num in enumerate(stringArray):
        # print(num)
        stringArray[pos] = int(num)
    return stringArray
