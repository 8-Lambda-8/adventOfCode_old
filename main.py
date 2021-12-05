import importlib.util
import os
from shutil import copyfile
import requests

year = "2021"
day = "5"
part = 1

dayFolder = year + "/" + day + "/"
dayModulePath = dayFolder+"day"+day+".py"
inputFilePath = dayFolder + "testInput"
inputFilePath = dayFolder + "input"
url = "https://adventofcode.com/" + year + "/day/" + day + "/input"

if not os.path.isdir(year):
    os.mkdir(year)

if not os.path.isdir(dayFolder):
    os.mkdir(dayFolder)

if not os.path.isfile(dayModulePath):
    copyfile("template.py", dayModulePath)

if not os.path.isfile(inputFilePath):
    print("Downloading input file")
    cookie = dict(session='53616c7465645f5fafc3cc256bae0cc356bf2cc0e1af8722a31a7565c65c61452da87f177688763043dc10f432a0939c')
    r = requests.get(url, cookies=cookie)
    open(inputFilePath, "wb").write(r.content)
    print("Download finished")
    print("")

spec = importlib.util.spec_from_file_location("day" + day, dayModulePath)
dayModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dayModule)
dayModule.run(part, inputFilePath)
