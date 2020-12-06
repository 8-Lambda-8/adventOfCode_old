def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n\n')
        # inputArray.remove("")

    if part == 1:
        questionYesCount = 0
        for group in inputArray:

            print(".")
            print(group)

            groupQuestionYes = []
            for person in group.split("\n"):
                for questionYes in person:
                    if questionYes not in groupQuestionYes:
                        groupQuestionYes.append(questionYes)
            print(len(groupQuestionYes))
            questionYesCount += len(groupQuestionYes)

        print("Solution:", questionYesCount)

    if part == 2:
        questionYesCount = 0
        for group in inputArray:

            print(".")
            print(group)

            groupQuestionYes = 0
            # for person in group.split("\n"):

            for i in range(ord('a'), ord('z')+1):
                if group.count(chr(i)) == len(group.split("\n")):
                    print(chr(i), group.count(chr(i)), str(len(group.split("\n"))))
                    groupQuestionYes += 1

                # for questionYes in person:
                #     if questionYes not in groupQuestionYes:
                #         groupQuestionYes.append(questionYes)

            questionYesCount += groupQuestionYes
        print("Solution:", questionYesCount)