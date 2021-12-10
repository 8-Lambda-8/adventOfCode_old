import time

def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        # inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        inputArray.remove("")
        # inputArray = list(map(int, inputArray)) # strings to int
        del inputFile
    startTime = time.perf_counter()

    if part == 1:
        count = {')': 0, ']': 0, '}': 0, '>': 0, }
        for line in inputArray:
            stack = []
            for char in line:
                if char in {'(', '[', '{', '<'}:
                    stack.append({'(': ')', '[': ']', '{': '}', '<': '>'}[char])
                if char in {')', ']', '}', '>'}:
                    if stack.pop() is not char:
                        count[char] += 1
                        # print("corrupted:", char)
                        # print(line)
                        break

        # print(count)
        solution = count[')'] * 3 + count[']'] * 57 + count['}'] * 1197 + count['>'] * 25137
        print(f"Solution Part 1: {solution}")

    if part == 2:
        autoCompleteScores = []
        for line in inputArray:
            stack = []
            for char in line:
                if char in {'(', '[', '{', '<'}:
                    stack.append({'(': ')', '[': ']', '{': '}', '<': '>'}[char])
                if char in {')', ']', '}', '>'}:
                    if stack.pop() is not char:
                        print("corrupted:", char)
                        break
            else:
                autoCompleteScore = 0
                # print("stack:", stack)
                for char in stack[::-1]:
                    autoCompleteScore *= 5
                    autoCompleteScore += {')': 1, ']': 2, '}': 3, '>': 4}[char]
                autoCompleteScores.append(autoCompleteScore)

        # print(autoCompleteScores)
        autoCompleteScores.sort()
        print("Solution Part 2:", autoCompleteScores[len(autoCompleteScores) // 2])

    print("calculating Time: {:10.3f} ms ".format((time.perf_counter() - startTime) * 1000))


if __name__ == "__main__":
    run(1, "input")
    run(2, "input")
