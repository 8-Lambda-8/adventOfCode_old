import time
import re

part_global = 0
def run(part, path):
    global part_global
    part_global = part
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1].replace(" ", "")
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
        del inputFile
    startTime = time.time()

    #if part == 1:
    solution = 0
    # print("end", calculateLine(inputArray[1]))
    for line in inputArray:
        lineSolution = calculateLine(line)
        print(lineSolution, "\n\n\n")
        solution += int(lineSolution)

    print("Solution:", solution)


    #    print("Solution:", "noSolution")

    print("calculating Time: ", (time.time() - startTime))


def getCloseParenthesesIndex(string, i):
    # print("getCloseParenthesesIndex", string)
    i += 1
    cnt = 1

    while cnt != 0:
        if string[i] == "(":
            cnt += 1
        elif string[i] == ")":
            cnt -= 1
        i += 1
        # print("cnt", cnt)
    return i


def stringInParentheses(string, i):
    lastIndex = getCloseParenthesesIndex(string, i)
    return string[i + 1:lastIndex - 1], lastIndex


def endOfNumber(string, i):
    ip = string.find("+", i)

    im = string.find("*", i)
    if ip == -1:
        i = im
    elif im == -1:
        i = ip
    else:
        i = min(ip, im)

    if i == -1:
        i = len(string)+1
    return i


def calculateLine(string):
    print("calc")
    global part_global

    while string.count("+") > 0 or string.count("*") > 0:

        print(string)
        i = 0

        operators = ["+", "("]
        if part_global == 1 or string.count("+") == 0:
            operators.append("*")

        while string[i] not in operators:
            i += 1

        if string[i] == "(":
            x, y = stringInParentheses(string, i)
            x = calculateLine(x)

            string = string[:i] + x + string[y:]
            continue

        if string[i + 1] == "(":
            x, y = stringInParentheses(string, i + 1)
            x = calculateLine(x)
            string = string[:i + 1] + x + string[y:]

        if string[i] == "+":
            end = endOfNumber(string, i + 1)
            start = max(string[:i].rfind("*")+1,
                        string[:i].rfind("(") + 1)

            string = string[:start] + str(int(string[start:i]) + int(string[i + 1:end])) + string[end:]
        elif string[i] == "*":  # and (string.count("+") == 0 or part_global == 1):
            end = endOfNumber(string, i + 1)
            string = str(int(string[:i]) * int(string[i + 1:end])) + string[end:]

    print("return calc", string)
    return string
