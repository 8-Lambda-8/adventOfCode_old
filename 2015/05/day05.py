def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split('\n')
        inputArray.remove("")

    vowels = ['a', 'e', 'i', 'o', 'u']
    forbiddenStrings = ['ab', 'cd', 'pq', 'xy']

    niceCount = 0
    if part == 1:
        for line in inputArray:
            vowelCount = 0
            for vowel in vowels:
                vowelCount += line.count(vowel)
            if vowelCount < 3:
                continue

            print("\n")
            print(line, vowelCount)

            if any(forbiddenString in line for forbiddenString in forbiddenStrings):
                continue

            if hasDoubleChar(line):
                niceCount += 1
                print("nice")
                # any (line.
        print("Solution:", niceCount)

    if part == 2:
        print("Solution:", "noSolution")


def hasDoubleChar(string):
    lastChar = '_'
    for char in string:
        if char is lastChar:
            print("hasDoubleChar:", string, "-", lastChar, char)
            return True
        else:
            lastChar = char
    return False


def hasAlphabetChar(string):
    lastChar = '_'
    for char in string:
        if ord(char) is ord(lastChar) + 1:
            print("hasAlphabetChar:", string, "-", lastChar, char)
            return True
        else:
            lastChar = char
    return False
