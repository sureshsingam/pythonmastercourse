import datetime

currentime = datetime.datetime.now()
currentime = currentime.strftime("%Y-%m-%d-%H-%M-%S-%f")
outputFile = open("mergedFile_{}.txt".format(currentime),"a")

for i in range(1,4):
    with open("file{}.txt".format(i)) as inputFile:
        outputFile.write(str(inputFile.readlines()[0])+"\n")

#Close the output file
outputFile.close()
