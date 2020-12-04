def run(part, path):
    with open(path, 'r') as file:
        inputArray = file.read().split('\n')

    print(inputArray[0])

    # parse Data
    inputArray = [line.replace(":", "").replace("-", " ").split(" ") for line in inputArray]

    print(inputArray[0])

    correctPasswords = 0

    # Part One
    if part == 1:
        for line in inputArray:
            charCount = line[3].count(line[2])
            if int(line[0]) <= charCount <= int(line[1]):
                correctPasswords = correctPasswords + 1

    # Part Two
    if part == 2:
        for line in inputArray:
            if (line[3][int(line[0]) - 1] is line[2]) is not (line[2] is line[3][int(line[1]) - 1]):
                correctPasswords += 1

    print(correctPasswords)
