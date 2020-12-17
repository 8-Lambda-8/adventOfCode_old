import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        del inputFile
    startTime = time.time()

    grid = {}

    if part == 1:

        maxCoordinates = [[-1, len(inputArray[0]) + 1], [-1, len(inputArray) + 1], [-1, 2]]

        for y, line in enumerate(inputArray):
            for x, cube in enumerate(line):
                grid[(x, y, 0)] = cube

        for z in range(-1, 1 + 1):
            print("\nz=", z)
            if (0, 0, z) not in grid:
                print("----\n")
                continue
            for y in range(0, 3):
                line = ""
                for x in range(0, 3):
                    line += grid[(x, y, z)]
                print(line)

        for cycle in range(6):
            print("\nCYCLE", cycle)
            # for cube in grid.copy():
            gridCopy = grid.copy()
            for z in range(maxCoordinates[2][0], maxCoordinates[2][1]):
                print("\nz=", z)
                for y in range(maxCoordinates[1][0], maxCoordinates[1][1]):
                    line = "" + str(y)
                    for x in range(maxCoordinates[0][0], maxCoordinates[0][1]):
                        cube = (x, y, z)
                        if cube not in gridCopy:
                            grid[cube] = "."
                            gridCopy[cube] = "."

                        if gridCopy[cube] == "#" and activeNeighborCount(gridCopy, cube) not in [2, 3]:
                            grid[cube] = "."
                        elif gridCopy[cube] == "." and activeNeighborCount(gridCopy, cube) == 3:
                            grid[cube] = "#"
                        line += grid[(x, y, z)]
                    print(line)

            # change Maximum
            for i in range(len(maxCoordinates)):
                maxCoordinates[i][0] -= 1
                maxCoordinates[i][1] += 1

        solution = 0
        for cube in grid:
            if grid[cube] == "#":
                solution += 1

        print("Solution:", solution)

    if part == 2:
        maxCoordinates = [[-1, len(inputArray[0]) + 1], [-1, len(inputArray) + 1], [-1, 2], [-1, 2]]

        for y, line in enumerate(inputArray):
            for x, cube in enumerate(line):
                grid[(x, y, 0, 0)] = cube

        for cycle in range(6):
            print("\nCYCLE", cycle)
            # for cube in grid.copy():
            gridCopy = grid.copy()
            for w in range(maxCoordinates[3][0], maxCoordinates[3][1]):
                for z in range(maxCoordinates[2][0], maxCoordinates[2][1]):
                    print("\nz=", z, ",w=", w)
                    for y in range(maxCoordinates[1][0], maxCoordinates[1][1]):
                        line = "" + str(y)
                        for x in range(maxCoordinates[0][0], maxCoordinates[0][1]):
                            cube = (x, y, z, w)
                            if cube not in gridCopy:
                                grid[cube] = "."
                                gridCopy[cube] = "."

                            if gridCopy[cube] == "#" and activeNeighborCount4D(gridCopy, cube) not in [2, 3]:
                                grid[cube] = "."
                            elif gridCopy[cube] == "." and activeNeighborCount4D(gridCopy, cube) == 3:
                                grid[cube] = "#"
                            line += grid[(x, y, z, w)]
                        print(line)

            # change Maximum
            for i in range(len(maxCoordinates)):
                maxCoordinates[i][0] -= 1
                maxCoordinates[i][1] += 1

        solution = 0
        for cube in grid:
            if grid[cube] == "#":
                solution += 1

        print("Solution:", solution)

    print("calculating Time: ", (time.time() - startTime))


def activeNeighborCount(grid, coordinates):
    count = 0
    for z in range(coordinates[2] - 1, coordinates[2] + 2):
        for y in range(coordinates[1] - 1, coordinates[1] + 2):
            for x in range(coordinates[0] - 1, coordinates[0] + 2):
                if (x, y, z) in grid:
                    if grid[(x, y, z)] == "#":
                        if (x, y, z) != coordinates:
                            count += 1

    return count


def activeNeighborCount4D(grid, coordinates):
    count = 0
    for w in range(coordinates[3] - 1, coordinates[3] + 2):
        for z in range(coordinates[2] - 1, coordinates[2] + 2):
            for y in range(coordinates[1] - 1, coordinates[1] + 2):
                for x in range(coordinates[0] - 1, coordinates[0] + 2):
                    if (x, y, z, w) in grid:
                        if grid[(x, y, z, w)] == "#":
                            if (x, y, z, w) != coordinates:
                                count += 1
    return count
