import time

from lib.myFunc import intArray


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        rulesList, messages = [x.split("\n") for x in inputFile.split('\n\n')]
        # inputArray.remove("")
        del inputFile
    startTime = time.time()

    rules = {}

    for rule in rulesList:
        ruleSplit = rule.split(": ")

        rules[int(ruleSplit[0])] = [intArray(x.split(" ")) for x in ruleSplit[1].split(" | ")]

    del rulesList

    print(rules)
    print(messages)

    def checkRule(ruleNr, prevRuleString, end):
        for possibleRule in rules[ruleNr]:
            if len(possibleRule) == 1:
                return rules[ruleNr][possibleRule][0]
            else:
                prevRuleString += checkRule(possibleRule, prevRuleString, False)  # rules[ruleNr][possibleRule][0]
                prevRuleString += checkRule(possibleRule, prevRuleString, True)
            if end:
                print()

    matchRuleCount = 0

    if part == 1:
        checkRule(0, "")
        finished = False
        # while not finished:

        print("Solution:", "noSolution")

    if part == 2:
        print("Solution:", "noSolution")

    print("calculating Time: ", (time.time() - startTime))
