from lib.myFunc import intArray
from sympy.ntheory.modular import crt
import time


def run(part, path):
    startTime = time.time()
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')

    earliestDeparture = int(inputArray[0])
    busIds = inputArray[1].split(",")

    timeDifference = 100
    busIdEarliest = 0
    if part == 1:

        for busId in busIds:
            if busId == "x":
                break
            busId = int(busId)
            i = 1
            while int(i * busId) < earliestDeparture:
                i += 1
            diff = i * busId - earliestDeparture
            if diff < timeDifference:
                timeDifference = diff
                busIdEarliest = busId

        print(busIdEarliest, timeDifference)
        solution = busIdEarliest * timeDifference

        print("Solution:", solution)
        print("calculating Time: ", (time.time() - startTime))

    if part == 2:
        bus_times = [(int(busId), -i) for i, busId in enumerate(busIds) if busId != 'x']
        busses, times = zip(*bus_times)

        print(bus_times)
        print(busses, times)
        solution = crt(busses, times)[0]
        print("Solution:", solution)
