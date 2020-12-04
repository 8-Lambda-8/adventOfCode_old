import hashlib


def run(part, path):
    with open(path, 'r', encoding='utf-8') as file:
        inputFile = file.read()
    md5_String = "1111111"
    i = 0
    if part == 1:
        while not md5_String.startswith("00000"):
            i += 1
            inputString = str(inputFile + str(i)).encode('utf-8')
            md5_String = str(hashlib.md5(inputString).hexdigest())
            print(inputString, ": ", md5_String)

        print("Solution:", i-1)

    if part == 2:
        while not md5_String.startswith("000000"):
            i += 1
            inputString = str(inputFile + str(i)).encode('utf-8')
            md5_String = str(hashlib.md5(inputString).hexdigest())
            print(inputString, ": ", md5_String)

        print("Solution:", i)
