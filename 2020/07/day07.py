def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        rules = inputFile.split('\n')
        # inputArray.remove("")

    myBagColor = "shiny gold"

    if part == 1:
        bagColorsEventuallyContain = [myBagColor]
        countBefore = 0
        while len(bagColorsEventuallyContain) > countBefore:
            countBefore = len(bagColorsEventuallyContain)
            print(bagColorsEventuallyContain)
            for rule in rules:
                splitRule = rule.split("contain")

                if any(color in splitRule[1] for color in bagColorsEventuallyContain):
                    print("can contain")
                    splitRule2 = rule.split(" ")
                    bagColor = splitRule2[0] + " " + splitRule2[1]
                    if bagColor not in bagColorsEventuallyContain:
                        bagColorsEventuallyContain.append(bagColor)

        bagColorsEventuallyContain.remove(myBagColor)
        print(bagColorsEventuallyContain)
        print("Solution:", len(bagColorsEventuallyContain))

    #     if part == 2:
    #         parentBagsList = [""]
    #         bagsList = [myBagColor]
    #         bagsCountList = [1]
    #         countBefore = 0
    #         checkedRules =[]
    #         while len(bagsList) > countBefore:
    #             countBefore = len(bagsList)
    #             for rule in rules:
    #                 splitRule = rule.split("contain")
    #                 if "no" in splitRule[1]:
    #                     checkedRules.append(rule)
    #                     continue
    #                 if any(color in splitRule[0] for color in bagsList):
    #                     for cols in splitRule[1].split(","):
    #                         splitRule2 = cols.split(" ")
    #                         splitRule2.remove("")
    #                         bagColor = splitRule2[1] + " " + splitRule2[2]
    #                         if rule not in checkedRules:
    #                             checkedRules.append(rule)
    #                             print(bagColor)
    #                             bagsList.append(bagColor)
    #                             bagsCountList.append(int(splitRule2[0]))
    #                             parentBagsList.append(splitRule[0].replace("bags", "")[:-2])
    #
    #
    #         print(len(parentBagsList), parentBagsList)
    #         print(len(bagsList), bagsList)
    #         print(len(bagsCountList), bagsCountList)
    #         print("")
    #
    #         individualBagCount = recursiveBagCount('', parentBagsList, bagsList, bagsCountList) - 2
    #
    #         print("Solution:", individualBagCount)
    #
    #
    # def recursiveBagCount(parentBag, parentBagsList, bagsList, bagsCountList):
    #     count = 0
    #     isParent = False
    #     for pos, bag in enumerate(bagsList):
    #         if parentBagsList[pos] == parentBag:
    #             isParent = True
    #             countThisCol = bagsCountList[pos] * (recursiveBagCount(bagsList[pos], parentBagsList, bagsList, bagsCountList))
    #             count = count + countThisCol
    #             print(pos, ":", bagsCountList[pos], "x", bag, "=",  countThisCol)
    #     if not isParent:
    #         return 1
    #
    #     return count + 1

    if part == 2:
        individualBagCount = recursiveBagCount(myBagColor, rules) - 1
        print("Solution:", individualBagCount)


def recursiveBagCount(parent, rules):
    count = 0

    for rule in rules:
        if rule.startswith(parent):
            if "no" in rule:
                return 1
            print(rule)
            for subBag in rule.split("contain")[1].split(","):
                subBag = subBag.replace(".", "").replace("bags", "").replace("bag", "")
                sp = subBag.split(" ")
                sp.remove("")
                colName = sp[1] + " " + sp[2]

                count += int(sp[0]) * recursiveBagCount(colName, rules)

    return count + 1
