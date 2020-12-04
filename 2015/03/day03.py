def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputArray = inputFile.split('\n')
    visited = []
    currentPos = [0, 0]

    print(currentPos)

    if part == 1:
        for move in inputFile:
            moveTo(move, currentPos)
            if currentPos not in visited:
                visited.append(currentPos.copy())

        print("Solution:", len(visited))

    currentPos2 = [0, 0]

    if part == 2:
        for i, move in enumerate(inputFile):
            if i % 2:
                moveTo(move, currentPos)
                if currentPos not in visited:
                    visited.append(currentPos.copy())
            else:
                moveTo(move, currentPos2)
                if currentPos2 not in visited:
                    visited.append(currentPos2.copy())
        print("Solution:", len(visited))


def moveTo(direction, pos):
    if direction == '>':
        pos[0] += 1
    elif direction == '<':
        pos[0] -= 1
    elif direction == '^':
        pos[1] += 1
    elif direction == 'v':
        pos[1] -= 1
