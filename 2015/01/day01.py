def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()

    if part == 1:
        cnt = inputFile.count("(")
        cnt -= inputFile.count(")")
        print("Solution:", cnt)

    if part == 2:
        cnt = 0
        for pos, char in enumerate(inputFile):
            if char == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt == -1:
                print("Solution:", pos + 1)
                break
