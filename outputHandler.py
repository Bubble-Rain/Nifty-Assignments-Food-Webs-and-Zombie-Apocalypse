import csv
import copy
import os

def findFileName(filePath):

    return copy.deepcopy(os.path.basename(filePath))


def outputName(filePath):

    fileName = findFileName(filePath)

    name, extension = copy.deepcopy(os.path.splitext(fileName))

    return name + '-out' + extension


def writeFile(outputPath, originalFilePath, outputText):

    textCopy = copy.deepcopy(outputText)

    fileName = outputName(originalFilePath)

    fullPath = outputPath + fileName

    with open(fullPath, "w") as writeFile:
        writeFile.write(outputText)




if __name__ == '__main__':

    writeFile("zombieFiles/Output/", "zombieFiles/Input/DataSet0.txt", "TestFile \n\n Tests: 1 \n Tests: 2 " )

    
