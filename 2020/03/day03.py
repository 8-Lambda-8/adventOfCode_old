def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split('\n')
    treeCount = 0
    X = 0
    if part == 1:
        for line in inputArray:
            s = list(line)
            if line[X] == '#':
                treeCount += 1
                s[X] = 'X'
            else:
                s[X] = 'O'
            print("".join(s))
            X += 3
            if X >= len(line):
                X = X - len(line)
        print("Solution:", treeCount)

    if part == 2:
        offsetList = [1, 3, 5, 7, 1]
        treeCount_ = 1
        treeCountList = []
        for offset in offsetList:
            X = 0
            treeCount = 0
            print(offset)
            for i in range(0, len(inputArray)):
                if i % 2 and offset == 1 and not treeCount_ == 1:
                    print(inputArray[i+1])
                    continue
                line = inputArray[i]
                s = list(line)
                if line[X] == '#':
                    treeCount += 1
                    s[X] = 'X'
                else:
                    s[X] = 'O'
                # print("".join(s))
                i += 1

                X += offset
                if X >= len(line):
                    X = X - len(line)

            treeCountList.append(treeCount)
            treeCount_ *= treeCount

            print("\n")
            print("\n")
        print(treeCountList)
        print("Solution:", treeCount_)
