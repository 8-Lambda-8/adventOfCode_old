import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        # inputArray = list(map(int, inputArray)) //strings to int
        del inputFile
    startTime = time.perf_counter()

    s = 1000
    thermalMap = [[0] * s for i in range(s)]

    for line in inputArray:
        start, end = line.split(" -> ")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))

        print(line)
        if start[0] == end[0]:  # horizontal Line
            x = start[0]
            if start[1] > end[1]:
                start[1], end[1] = end[1], start[1]
            for y in range(start[1], end[1] + 1):
                # print(x, " ", y)
                thermalMap[y][x] += 1
        elif start[1] == end[1]:  # vertical Line
            y = start[1]
            if start[0] > end[0]:
                start[0], end[0] = end[0], start[0]
            for x in range(start[0], end[0] + 1):
                # print(x, " ", y)
                thermalMap[y][x] += 1
        elif part == 2:

            if start[0] > end[0]:
                start[0], end[0] = end[0], start[0]
                start[1], end[1] = end[1], start[1]

            for o in range(end[0] - start[0] + 1):
                # print(o)
                x = start[0] + o
                if start[1] < end[1]:
                    y = start[1] + o
                else:
                    y = start[1] - o
                thermalMap[y][x] += 1

    solution = 0

    for y in thermalMap:
        # print("".join(list(map(str, y))))
        for x in y:
            solution += 1 if x > 1 else 0

    print("Solution Part", part, solution)

    print("calculating Time:", (time.perf_counter() - startTime) * 1000, "ms")


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
