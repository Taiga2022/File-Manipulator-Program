import sys

# with open(sys.argv[2]) as f:
#     print(f.read())

class InputFile:
    def __init__(self):
        self.inputPath=sys.argv[2]

    def read(self):
        with open(self.inputPath) as f:
            return f.read()

    def duplicate(self):
        duplicateNumber=sys.argv[3]
        inputFileValue=self.read()
        for i in range(0,int(duplicateNumber)):
            with open(self.inputPath,'a') as f:
                f.write(inputFileValue)

    def replace(self):
        inputFileValue=self.read()
        with open(self.inputPath,'w') as f:
            f.write(inputFileValue.replace(sys.argv[3],sys.argv[4]))



class OutputFile:
    def __init__(self):
        self.outputPath=sys.argv[3]

    def reverse(self,inputFileValue):
        with open(self.outputPath,'w') as f:
            f.write(inputFileValue[::-1])

    def copy(self,inputFileValue):
        with open(self.outputPath,'w') as f:
            f.write(inputFileValue)

if __name__ == '__main__':
    inputFile=InputFile()
    command=sys.argv[1]
    inputCommands={'duplicate-contents':inputFile.duplicate,'replace-string':inputFile.replace}
    if command in inputCommands:
        inputCommands[command]()
    else:
        outputFile=OutputFile()
        outputCommands={'reverse':outputFile.reverse,'copy':outputFile.copy}
        outputCommands[command](inputFile.read())