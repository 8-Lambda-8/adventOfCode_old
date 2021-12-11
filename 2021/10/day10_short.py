import time

if __name__ == "__main__":
    with open("input", 'r') as file:
        inputFile = file.read()
        inputArray = inputFile.split('\n')
        inputArray.remove("")
        del inputFile
    startTime = time.perf_counter()

    autoCompleteScores = []
    count = {')': 0, ']': 0, '}': 0, '>': 0, }
    for line in inputArray:
        stack = []
        for char in line:
            if char in {'(', '[', '{', '<'}:
                stack.append({'(': ')', '[': ']', '{': '}', '<': '>'}[char])
            if char in {')', ']', '}', '>'}:
                if stack.pop() is not char:
                    count[char] += 1
                    break
        else:
            autoCompleteScore = 0
            for char in stack[::-1]:
                autoCompleteScore *= 5
                autoCompleteScore += {')': 1, ']': 2, '}': 3, '>': 4}[char]
            autoCompleteScores.append(autoCompleteScore)

    solution = count[')'] * 3 + count[']'] * 57 + count['}'] * 1197 + count['>'] * 25137
    print(f"Solution Part 1: {solution}")

    autoCompleteScores.sort()
    print(f"Solution Part 2: {autoCompleteScores[len(autoCompleteScores) // 2]}")

    print(f"calculating Time: {((time.perf_counter() - startTime) * 1000):10.3f} ms ")
