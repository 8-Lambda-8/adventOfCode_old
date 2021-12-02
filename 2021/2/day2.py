import time


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        # inputArray = list(map(int, inputArray)) //strings to int
        del inputFile
    startTime = time.perf_counter()

    X = 0
    Y = 0

    if part == 1:
        for line in inputArray:
            line = line.split(" ")
            if line[0] == "forward":
                X += int(line[1])
            if line[0] == "down":
                Y += int(line[1])
            if line[0] == "up":
                Y -= int(line[1])

        print("Solution Part 1:", X * Y)

    aim = 0

    if part == 2:
        for line in inputArray:
            line = line.split(" ")
            if line[0] == "forward":
                X += int(line[1])
                Y += int(line[1])*aim
            if line[0] == "down":
                aim += int(line[1])
            if line[0] == "up":
                aim -= int(line[1])



        print("Solution Part 2:", X*Y)

    print("calculating Time: ", (time.perf_counter() - startTime))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
