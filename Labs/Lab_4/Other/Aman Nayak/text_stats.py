#!/usr/bin/env python3

import sys

def inputValidation():
    ipLen = len(sys.argv)
    if ipLen < 2:
        print("Please provide file name in order to process it")
        return False
    
    if ipLen >=2 :
        #try : 
        file = sys.argv[1]
        #File exit test 
        import os.path
        if os.path.isfile(file):
            return True
        else: 
            print(f"The file {file} does not exist!")
            return False


def preProcessing(ipFile , calcAlpha = False):
    #Function read file and make list of all words and count alphabets if calcAlpha is set True.
    if calcAlpha == True:        
        validAlpha = "abcdefghijklmnopqrstuvwxyz" 
        alphaCount = {}  
        #ASCII for small caps ranges from 97:a to 122:z
        for i in range(97,123):
            aplha = (chr(i))
            alphaCount[aplha] = 0
    
    #reading file for alphabets frequency 
   
    import codecs   
    listOfWordsToProcess = []
    with codecs.open(ipFile ,encoding='utf-8' , errors= 'ignore') as file:
        for line in file: 
            lWords = line.split()        
            for words in lWords:
                #this create list of words unlike above line where we had complete lines in line
                listOfWordsToProcess.append(words)
                
                if calcAlpha == True:                    
                    wAlpha = list(words) # break words in alphabet 
                    #print(wAlpha)
                    for char in wAlpha:
                        if char.isalpha():
                            if char.isupper():
                                char = char.lower()
                            if char in validAlpha:
                                alphaCount[char] += 1
    if calcAlpha == True:
        return listOfWordsToProcess , alphaCount
    else:
        return listOfWordsToProcess

def filterWord(wlist):
    #    Function read the list of word and filter it for alien character and return two 
    #    outputs, containing counter of words and list of words in order of there 
    #    occurrence which can be further used for calculation of top words along with words 
    #    associated with them.
    
    wlist = [word.lower() for word in wlist]
    wListCountDict = {} 
    charToRemove = ['"' , '\ufeff', '\r' , '-' , '_' , 'c’' , ';' , '’' ,'-' , '\n' ,'\t' , '?' , '&' , '#' , '$' ,  '.' , ',' , ']' , '[' , '!' , '&' , '(' , ')','”' , '%', "'"]
    #filtered list of words which do not contain junk characters
    filteredList = []
    
    for word in wlist:
        #filter Alien characters 
        for char in charToRemove:
                word = word.replace(char , "") 
        
        if not word.isdigit():               
            if word != "" :                 
                filteredList.append(word)
                if word in wListCountDict:
                    wListCountDict[word] += 1
                else:                    
                    wListCountDict[word] = 1     
    return wListCountDict,filteredList


def uniqueWordFollowingWord(filteredList):
    uniqueWord = list(set(filteredList))
    uniqueWordDict = dict.fromkeys(uniqueWord)
    for index , word in enumerate(filteredList):
        try:   
            if word in uniqueWordDict:        
                nextWord = filteredList[index + 1]
                childDict = uniqueWordDict[word]            
                if childDict is None:
                    #create empty child dict if not already exit
                    childDict = {}
                if nextWord in childDict:
                    childDict[nextWord] += 1
                else:
                    childDict[nextWord] = 1
                
                uniqueWordDict[word] = childDict            
        except Exception:
            pass    
        
    return uniqueWordDict


def topFiveWords(wListCountDict):    
    #returns top 5 words out of all words we have 
    sort = sorted(wListCountDict.items() , key = lambda x : x[1] , reverse=True)[0:5]    
    words = [word[0] for word in sort]
    count = [count[1] for count in sort]
    return words , count

def nextOccuranceWords(ipWord,filteredList):
    #use filtered list to find next word post word of intreset as our filtered list was created in sequence of 
    #occurence of words 
    
    findIndexes = [index for index , word in enumerate(filteredList) if word == ipWord]
    findIndexes_next = [index + 1 for index in findIndexes]
    followWords = [filteredList[index] for index in findIndexes_next]
    return followWords


def frequencyFollowingWords(nextWord):
    #calculate frequency of intrested word
    hashTable = {}
    for word in nextWord:
        if word in hashTable:
            hashTable[word] +=1
        else:
            hashTable[word] = 1

    return hashTable


def topFollowingWOrds(wordList ,filteredList):
    #return dictoniary of word along with its top 3 following word
    from collections import Counter
    fWords = {}
    for word in wordList:
        nOccurWOrds = nextOccuranceWords(word , filteredList)
        freq = frequencyFollowingWords(nOccurWOrds)
        counter = Counter(freq)
        reOrder = counter.most_common()
        fWords.update({word:reOrder[0:3]})
    return fWords


   
def main():    
    #Exception Validation 
    if inputValidation():
        #Read file if initial validations are cleared
        filename = sys.argv[1]
        
    
        listOfWordsToProcess , alphaCount = preProcessing(filename , calcAlpha = True)
        #Reorder Alphabets
        sortedAlpha = sorted(alphaCount.items() , key = lambda x : x[1] , reverse=True)
        
        
        wListCountDict , filteredList = filterWord(listOfWordsToProcess)
#        totalWords = len(filteredList)
#        uniqueWOrds = len(set(filteredList))
        
        
        top5w , top5wc = topFiveWords(wListCountDict)
        
        #get top5 words following 3 words 
        top5WordFollower = topFollowingWOrds(top5w,filteredList)
        
        
        if(len(sys.argv) > 2):
            fileDetails = sys.argv[2]
            with open(fileDetails,'w') as f:
                f.write("Alphabet Frequency")
                f.write("\n")
                #f.write("Alphabet frequency in order of most to least is " , "\n")
                for alpha , freq in sortedAlpha:
                    wString = alpha + "      " + str(freq)
                    f.write(wString)
                    f.write( "\n") 
                    
                f.write("\n")
                f.write("-----------------------------------------------------")
                f.write("\n")
                f.write(f"\nThe total number of words in the file are:  {len(filteredList)}\n")
                f.write("\n")
                f.write("-----------------------------------------------------")
                f.write("\n")
                f.write(f"\nThe total number of unique words in the file are:  {len(set(filteredList))}\n")
                f.write("-----------------------------------------------------")
                f.write("\n")
                f.write("\nOcurrences of the top 5 common words followed by their top 3 successors:\n")
                
                count = 0
                for key , val in top5WordFollower.items():
                    f.write("\n")
                    masterWord = key + "(" + str(top5wc[count]) + " occurrence)"  
                    f.write(masterWord)
                    f.write("\n")
                    for v in val:
                        assoWords =  "-- " + v[0] + " , " + str(v[1])
                        f.write(assoWords)
                        f.write("\n")
                        
                    count += 1 
                
                f.write("\n")
                f.write("-----------------------------------------------------")
                f.write("\n")
                f.write("*****************End of File*************************")
        else: 
            print("-----------------------------------------------------")
            print("Alphabet frequency in order of most to least is " , "\n")
            #[(print(alpha , count)) for alpha , count in sortedAlpha]
            print("Alphabet Frequency")
            for alpha , freq in sortedAlpha:
                print(alpha , "      " ,  freq)
            
            print("\n")
            print("-----------------------------------------------------")
            print("\n")
            print(f"\nThe total number of words in the file are: ", {len(filteredList)},"\n")
            print("\n")
            print("-----------------------------------------------------")
            print("\n")
            print("\nThe total number of unique words in the file are: ", {len(set(filteredList))},"\n")
            print("-----------------------------------------------------")
            print("\n")
            print("\nOcurrences of the top 5 common words followed by their top 3 successors:\n")
           
            count = 0
            for key,val in top5WordFollower.items():
                print(key , "(" , top5wc[count] , " occurrence)" )
                for v in val:
                    #print('\n'.join(map(str,v)))
                    print("-- " , v[0] , " , " , v[1])
                    
                count += 1 
            
            print("\n")
            print("-----------------------------------------------------")
            print("\n")
            print("*****************End of File*************************")
            
    else: 
        raise ValueError('Encountered Error, read above message')

       
#Run directly 
if __name__ == "__main__":
    main()