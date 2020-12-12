import time

from lib.myFunc import replaceCharAt, compareTuple


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
    startTime = time.time()

    area = (len(inputArray[0]) - 1, len(inputArray) - 1)
    # print(area)
    occupiedSeats = 0
    occupiedSeatsLast = -1
    roundCount = 0
    arrayNextRound = inputArray.copy()

    neighbors = lambda x_, y_: [(x2, y2) for x2 in range(x_ - 1, x_ + 2)
                                for y2 in range(y_ - 1, y_ + 2)
                                if (-1 < x_ <= area[0] and
                                    -1 < y_ <= area[1] and
                                    (x_ != x2 or y_ != y2) and
                                    (0 <= x2 <= area[0]) and
                                    (0 <= y2 <= area[1]))]


    def visibles(x_, y_):
        visibleList = neighbors(x_, y_)

        for pos, neighbor_ in enumerate(visibleList):

            offsets = (neighbor_[0] - x_, neighbor_[1] - y_)
            if neighbor_[1] > len(inputArray):
                break
            while inputArray[neighbor_[1]][neighbor_[0]] == '.' \
                    and compareTuple((-1, -1), (len(inputArray[0]), len(inputArray)), neighbor_):
                # and (0, 0) < neighbor_ < (len(inputArray[0]) - 2, len(inputArray) - 2):

                neighbor_ = list(neighbor_)
                neighbor_[0] += offsets[0]
                neighbor_[1] += offsets[1]
                neighbor_ = tuple(neighbor_)
                # if not (0, 0) < neighbor_ < (len(inputArray[0]) - 2, len(inputArray) - 2):
                if not compareTuple((-1, -1), (len(inputArray[0]), len(inputArray)), neighbor_):
                    # print("out Of bounds")
                    break

                visibleList[pos] = neighbor_
        # print(visibleList)
        return visibleList

    if part == 1:
        while not occupiedSeats == occupiedSeatsLast:
            occupiedSeatsLast = occupiedSeats
            print(roundCount)
            for y in range(len(inputArray)):
                print(inputArray[y])
                for x in range(len(inputArray)):
                    neighborCount = 0
                    if inputArray[y][x] == 'L':  # seat Empty

                        neighbors_ = neighbors(x, y)
                        for neighbor in neighbors_:
                            # print(neighbor)
                            neighborSeat = inputArray[neighbor[1]][neighbor[0]]
                            if not neighborSeat == '#':
                                neighborCount += 1

                        if neighborCount == len(neighbors_):
                            arrayNextRound[y] = replaceCharAt(arrayNextRound[y], x, '#')
                            occupiedSeats += 1

                    elif inputArray[y][x] == '#':  # seat Occupied

                        for neighbor in neighbors(x, y):
                            # print(neighbor)
                            neighborSeat = inputArray[neighbor[1]][neighbor[0]]
                            if neighborSeat == '#':
                                neighborCount += 1
                        if neighborCount > 3:
                            # print(neighborCount)
                            arrayNextRound[y] = replaceCharAt(arrayNextRound[y], x, 'L')
                            occupiedSeats -= 1
            inputArray = arrayNextRound.copy()
            print("")
            print("")
            roundCount += 1

        print("Solution:", occupiedSeats)

    if part == 2:
        while not occupiedSeats == occupiedSeatsLast:
            occupiedSeatsLast = occupiedSeats
            print(roundCount)
            for y in range(len(inputArray)):
                print(inputArray[y])
                for x in range(len(inputArray)):
                    visibleCount = 0
                    if inputArray[y][x] == 'L':  # seat Empty

                        visibles_ = visibles(x, y)
                        for visible in visibles_:
                            # print(neighbor)
                            visibleSeat = inputArray[visible[1]][visible[0]]
                            if not visibleSeat == '#':
                                visibleCount += 1

                        if visibleCount == len(visibles_):
                            arrayNextRound[y] = replaceCharAt(arrayNextRound[y], x, '#')
                            occupiedSeats += 1

                    elif inputArray[y][x] == '#':  # seat Occupied

                        for visible in visibles(x, y):
                            # print(neighbor)
                            visibleSeat = inputArray[visible[1]][visible[0]]
                            if visibleSeat == '#':
                                visibleCount += 1
                        if visibleCount > 4:
                            # print(neighborCount)
                            arrayNextRound[y] = replaceCharAt(arrayNextRound[y], x, 'L')
                            occupiedSeats -= 1
            inputArray = arrayNextRound.copy()
            print("")
            print("")
            roundCount += 1

        print("Solution:", occupiedSeats)

    print("calculating Time: ", (time.time() - startTime))
