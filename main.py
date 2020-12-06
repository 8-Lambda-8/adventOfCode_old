import importlib.util
import os
from shutil import copyfile
import requests


year = "2020"
day = "06"
part = 2

dayFolder = year + "/" + day + "/"
dayModulePath = dayFolder+"day"+day+".py"
inputFilePath = dayFolder + "input"
url = "https://adventofcode.com/" + year + "/day/" + str(int(day)) + "/input"

if not os.path.isdir(dayFolder):
    os.mkdir(dayFolder)

if not os.path.isfile(dayModulePath):
    copyfile("template.py", dayModulePath)

if not os.path.isfile(inputFilePath):
    print("Downloading input file")
    cookie = dict(session='53616c7465645f5f20dc83dec9285177bd2c1acd62c066e088229dcfc8489b7aaa4385c4ebeee590121c54dfec0855a2')
    r = requests.get(url, cookies=cookie)
    open(inputFilePath, "wb").write(r.content)
    print("Download finished")
    print("")

spec = importlib.util.spec_from_file_location("day" + day, dayModulePath)
dayModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dayModule)
dayModule.run(part, inputFilePath)

# os.system(year + "/" + day + "/day" + day + ".py")
