import time


def markBingoCard(bingoCard, n):
    for y, line in enumerate(bingoCard):
        for x, col in enumerate(line):
            if col == n:
                bingoCard[y][x] = "X"
    return bingoCard


def checkBingoCard(bingoCard):
    # check lines
    for line in bingoCard:
        if line.count("X") >= len(line):
            return True

    cols = [0] * 5
    for line in bingoCard:
        for i, col in enumerate(line):
            if col == "X":
                cols[i] += 1
    if any(col >= len(bingoCard) for col in cols):
        return True
    return False


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n\n')
        # inputArray.remove("")
        # inputArray = list(map(int, inputArray)) //strings to int
        del inputFile
    startTime = time.perf_counter()
    numbers = inputArray[0].split(",")
    del inputArray[0]

    bingoCards = []
    for card in inputArray:
        bingoCards.append(([list(filter(lambda l: l != "", line.split(" "))) for line in card.split("\n")]))

    print(bingoCards)

    if part == 1:
        winningCard = []
        lastNr = 0
        for n in numbers:
            for i, bingoCard in enumerate(bingoCards):
                bingoCards[i] = markBingoCard(bingoCard, n)
                if checkBingoCard(bingoCard):
                    winningCard = bingoCard
                    lastNr = n
                    print("WIN", i)
                    break
            else:
                continue
            break

        print(winningCard)
        solution = 0
        for line in winningCard:
            for col in line:
                if col != "X":
                    solution += int(col)
        solution *= int(lastNr)
        print("Solution Part 1:", solution)

    if part == 2:

        lastWinningCard = []
        lastNr = 0
        winningCards = []
        for n in numbers:
            for i, bingoCard in enumerate(bingoCards):
                if not (any(winningCard == i for winningCard in winningCards)):
                    bingoCards[i] = markBingoCard(bingoCard, n)
                    if checkBingoCard(bingoCard):
                        winningCards.append(i)
                        lastWinningCard = bingoCard
                        lastNr = n
                        print("last WIN", i)

        print(lastWinningCard)
        solution = 0
        for line in lastWinningCard:
            for col in line:
                if col != "X":
                    solution += int(col)
        print(solution)
        print(lastNr)
        solution *= int(lastNr)

        print("Solution Part 2:", solution)

    print("calculating Time: ", (time.perf_counter() - startTime) / 1000, "ms")


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
