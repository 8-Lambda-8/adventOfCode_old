def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")

    accValue = 0
    runList = []

    if part == 1:

        i = 0
        while i < len(inputArray):

            print(inputArray[i], "|", i, accValue)

            if i in runList:
                print("Second Run:", i, ":", accValue)
                break
            runList.append(i)
            if inputArray[i].startswith("acc"):
                accValue += int(inputArray[i].split(" ")[1])
                i += 1
            elif inputArray[i].startswith("jmp"):
                i += int(inputArray[i].split(" ")[1])
            elif inputArray[i].startswith("nop"):
                i += 1

        print("Solution:", accValue)

    if part == 2:

        for change in range(len(inputArray)):
            if "jmp" not in inputArray[change]:
                continue

            modInputArray = inputArray.copy()

            runList = []
            accValue = 0

            print("")
            print("change:", change)
            print("replace", modInputArray[change])
            modInputArray[change] = modInputArray[change].replace("jmp", "nop")
            print("with", modInputArray[change])
            print("")

            i = 0
            while i < len(modInputArray):

                print(modInputArray[i], "|", i, accValue)

                if i in runList:
                    print("Second Run:", i, ":", accValue)
                    break
                runList.append(i)
                if modInputArray[i].startswith("acc"):
                    accValue += int(modInputArray[i].split(" ")[1])
                    i += 1
                elif modInputArray[i].startswith("jmp"):
                    i += int(modInputArray[i].split(" ")[1])
                elif modInputArray[i].startswith("nop"):
                    i += 1
            else:
                break

        print("Solution:", accValue)
