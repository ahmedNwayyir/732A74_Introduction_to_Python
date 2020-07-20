#!/usr/bin/env python3

import sys
import string

def lettersort(words):
    print("frequency table for alphabetic letters:")
    d = {}
    for word in words:
        for c in word:
            if c.isalpha():
                d[c]=d.setdefault(c,0)+1
    return d


def uniquewords(words):
    u_words = {a for a in words}
    return u_words

def followingwords(words):
    d = {}
    
    #dict of following words of every word
    for counter, value in enumerate(words):
        if counter == len(words)-1:
            pass
        else:
            d[value][words[counter+1]] = d.setdefault(value,{}).setdefault(words[counter+1],0)+1
    return d

def wordoccurences(words): 
    #dict of word occurences
    o = {}
    for w in words:
        o[w]=o.setdefault(w,0)+1
    return o



def programm(filename):
    try: 
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("The file does not exist!")

    else:
        if len(sys.argv) == 3:
            orig_out = sys.stdout
            f = open(sys.argv[2], 'w')
            sys.stdout = f
        #preprocessing words
        words = contents.split()
        words = [a.lower() for a in words]
        words = [a.translate(str.maketrans('','',string.punctuation)) for a in words]
        number_words = len(words)
        
        #-------
        
        for k, v in sorted(lettersort(words).items(), key=lambda t: t[1], reverse=True):
            print(k,v)
        
        print()
        print("number of words: ", number_words)
        print("number of unique words",len(uniquewords(words)))
        print()
        #-------

        o = wordoccurences(words)
        d = followingwords(words)
        for ko, vo in sorted(o.items(), key=lambda t: t[1], reverse=True)[:5]:
        #output of following words
            print(ko, " (", vo, " occurences)")    
            for k, v in sorted(d[ko].items(), key=lambda t: t[1], reverse=True)[:3]:
                print("--",k,v)
        
        print("")      
        if len(sys.argv) == 3:
            sys.stdout = orig_out
            f.close()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please add name of textfile!")
    else:
        programm(sys.argv[1])
        #implement for multiple args

else:
    print("I was imported!")