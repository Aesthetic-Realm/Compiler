import os


def getSentenceInput(method=0):
    if method == 0:
        string = input("Please input a sentence: ")
        file = open("sentence.txt", "w")
        file.write(string + "\n")
        file.close()
        return 0
    else:
        file = open("sentence.txt", "r")
        if not file:
            print("Error: cannot open file sentence.txt")
            return -1
        file.close()
        return 0


def callLex(inputString):
    exeFile = "Lex.exe"
    lexResultList = os.popen(exeFile + " " + inputString).read()
    return lexResultList

def processLexResult(lexResultList):
    # ignore first line and last line
    formalList = lexResultList.split("\n")[1:-1]
    resultList=[]
    for item in formalList:
        item = item.split('\t')[1]
        resultList.append(item)
        # print(item.split('\t')[1])
        
    print('formalList: ', resultList)
    return resultList
    
    
    
    
# getSentenceInput(1)
# lexResultList=(callLex("sentence.txt"))
# print(processLexResult(lexResultList))