import re


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        raw_passportArray = inputFile.split('\n\n')

    passportFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    requiredPasswordFields = passportFields.copy()
    requiredPasswordFields.remove("cid")

    validPassportCount = 0
    passportArray = []
    for pos, passport in enumerate(raw_passportArray):
        passport = passport.replace(" ", "\n").split("\n")
        if "" in passport:
            passport.remove("")
        print(passport)
        passportArray.append(passport)

    if part == 1:
        for passport in passportArray:
            print("")
            print(passport)
            validFieldCount = 0
            for field in passport:
                if any(requiredPasswordField in field for requiredPasswordField in requiredPasswordFields):
                    validFieldCount += 1

            if validFieldCount >= len(requiredPasswordFields):
                validPassportCount += 1

        print("Solution:", validPassportCount)

    if part == 2:
        for passport in passportArray:
            print("")
            print(passport)
            validFieldCount = 0
            for field in passport:
                if any(requiredPasswordField in field for requiredPasswordField in requiredPasswordFields):
                    field = field.split(":")
                    if field[0] == "byr":
                        if 1920 <= int(field[1]) <= 2002:
                            validFieldCount += 1
                            print(field, True)
                    elif field[0] == "iyr":
                        if 2010 <= int(field[1]) <= 2020:
                            validFieldCount += 1
                            print(field, True)
                    elif field[0] == "eyr":
                        if 2020 <= int(field[1]) <= 2030:
                            validFieldCount += 1
                            print(field, True)
                    elif field[0] == "hgt":
                        if field[1].endswith("cm"):
                            hgt = field[1].replace("cm", "")
                            if 150 <= int(hgt) <= 193:
                                validFieldCount += 1
                                print(field, True)
                        elif field[1].endswith("in"):
                            hgt = field[1].replace("in", "")
                            if 59 <= int(hgt) <= 76:
                                validFieldCount += 1
                                print(field, True)
                    elif field[0] == "hcl":
                        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', field[1]):
                            validFieldCount += 1
                            print(field, True)
                    elif field[0] == "ecl":
                        if any(ecl == field[1] for ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                            validFieldCount += 1
                            print(field, True)
                    elif field[0] == "pid":
                        if len(field[1]) == 9 and field[1].isnumeric():
                            validFieldCount += 1
                            print(field, True)
            print(validFieldCount)
            if validFieldCount >= len(requiredPasswordFields):
                validPassportCount += 1

        print("Solution:", validPassportCount)
