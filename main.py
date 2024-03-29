from GrammarInputProcess import getInput,getFirstSet,transformInput
from SentenceFormaler import getSentenceInput,callLex,processLexResult

inputs, keywordsList = getInput(1)  # input grammar
grammar = transformInput(inputs)  # transform grammar to a list of productions
firstSet = getFirstSet(grammar, keywordsList)  # get first set

getSentenceInput(1)  # input sentence, save to file sentence.txt
lexResultList = callLex("sentence.txt")  # call Lex.exe to analyze input
formalList = processLexResult(lexResultList)  # get formal sentence
