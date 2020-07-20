#!/usr/bin/env python3

import sys
import random
import text_stats as ts

#def fecthWordRandomly(startWord , filteredList):
#    nOccurWOrds = ts.nextOccuranceWords(startWord , filteredList)
#    freq = ts.frequencyFollowingWords(nOccurWOrds)
#    totalSum = len(nOccurWOrds)
#    normalize_frequency = {key:float(value)/totalSum for key,value in freq.items()}
#    return (random.choices(list(normalize_frequency.keys()), weights = normalize_frequency.values(), k = 1)[0])

def fecthWordRandomly(startWord , uniqueWordDict):
    freq =  uniqueWordDict[startWord]
    totalSum = len(freq.keys())
    normalize_frequency = {key:float(value)/totalSum for key,value in freq.items()}
    return (random.choices(list(normalize_frequency.keys()), weights = normalize_frequency.values(), k = 1)[0])


def text_generation(ipFile , startWord , maxWord):
    
    listOfWordsToProcess = ts.preProcessing(ipFile)    
    wListCountDict , filteredList = ts.filterWord(listOfWordsToProcess)
    uniqueWordDict = ts.uniqueWordFollowingWord(filteredList)
    
    
    msgArray = []
    for i in range(int(maxWord)):
        startWord = fecthWordRandomly(startWord , uniqueWordDict)
        msgArray.append(startWord)
    
    genText = " ".join(msgArray)
    
    return genText
    
    
def main():
    if len(sys.argv) < 2:
        raise NameError("Please provide input text file a, starting word and maximum number of words")
    elif(len(sys.argv) < 3):
        raise NameError("Please provide starting word and maximum number of words")
    elif(len(sys.argv) < 4):
        raise NameError("Please provide maximum number of words")
        
    ipFile = sys.argv[1]
    startWord = sys.argv[2]
    maxWord = sys.argv[3]
    
    generated = text_generation(ipFile , startWord , maxWord)
    
    print("-------------------------------------------------------")
    print("/n")
    
    print(generated)
    
    print("/n")    
    print("-------------------------------------------------------")
    

if __name__ == "__main__" :
    main()   