import time
import re
from lib.myFunc import intArray
from collections import defaultdict


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n\n')

    startTime = time.time()

    rulesList = inputArray[0].split("\n")
    rules = defaultdict(list)
    for rule in rulesList:
        ruleSplit = rule.split(":")
        ruleName = ruleSplit[0]
        for r in re.findall(r"\d+\-\d+", ruleSplit[1]):
            rules[ruleName].append(tuple(int(x) for x in r.split("-")))
    del rulesList

    myTicket = intArray(inputArray[1].replace("your ticket:\n", "").split(","))

    inputArray[2] = inputArray[2].split("\n")
    del inputArray[2][0]
    tickets = [intArray(line.split(",")) for line in inputArray[2]]

    print(rules)
    print(myTicket)
    print(tickets)

    wrongValues = []

    for ticket in tickets[:]:
        for value in ticket:
            for field in rules:
                if value in range(rules[field][0][0], rules[field][0][1] + 1) or \
                        value in range(rules[field][1][0], rules[field][1][1] + 1):
                    # print(value, "in")
                    break
            else:
                wrongValues.append(value)
                tickets.remove(ticket)

    if part == 1:
        print(wrongValues)
        print("Solution:", sum(wrongValues))

    if part == 2:
        possibleFields = {i: set(rules.keys()) for i in range(len(tickets[0]))}
        for ticket in tickets:
            for pos, value in enumerate(ticket):
                for field in rules:

                    if value in range(rules[field][0][0], rules[field][0][1] + 1) or \
                            value in range(rules[field][1][0], rules[field][1][1] + 1):
                        continue
                    else:
                        # print("invalid: ", pos, value, field)
                        possibleFields[pos].discard(field)

        for i in sorted(possibleFields, key=lambda k: len(possibleFields[k])):
            thisField = next(iter(possibleFields[i]))
            for j in possibleFields:
                if i != j:
                    possibleFields[j].discard(thisField)

        solution = 1
        for i in possibleFields:
            if possibleFields[i].pop().startswith("departure"):
                solution *= myTicket[i]

        print("Solution:", solution)

    print("calculating Time: ", (time.time() - startTime))
