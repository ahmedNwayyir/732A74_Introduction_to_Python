#!/usr/bin/env python3
import sys
import os
import json
from collections import OrderedDict



alphabets_upplow = set('abcdefghijklmnopqrstuvwxyz')
# ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def filter_string(text):
    line = text.lower()
    line = ''.join(filter(alphabets_upplow.__contains__, line))
    return line

def number_words(words): 
    dictionary = {}
    for i in range(len(words)):
        word1 = words[i]
        if(word1 in dictionary):
            dictionary[word1]['Frequency'] += 1
        else:
            dictionary[word1] ={} 
            dictionary[word1]['Frequency'] = 1

        if(i < len(words)-1) :
            word2 = words[i+1]
            if(word2 in dictionary[word1]):
                dictionary[word1][word2] += 1
            else:
                dictionary[word1][word2] =1
    return dictionary

def dictionary_output(dict,n):
    for key,value in dict[:n]:
        print('{words} : {Number of times}'.format(word=key,count=value))


def output_file(output,line):
    with open(output, 'a+') as file:
        file.write(line)

def alpha_count(content):
    alpha_dictionary = {}
    for word in content:
        if(len(word)>1):
            word = word.replace(" ", "")
            alphabets = list(word)
            
            for alpha in alphabets:
                alpha_dictionary[alpha] = alpha_dictionary.get(alpha, 0) + 1

    return alpha_dictionary


if __name__ == '__main__':
    result = ''
    file_name = None
    output = False
    out_file=None
    args = len(sys.argv)-1
    if(args >= 2):
        file_name = sys.argv[1]
        output = True
        out_file= sys.argv[2]
        print("for stats please check {file}".format(file=out_file))

    elif(args >= 1 ):
        file_name = sys.argv[1]
    else:
        print("Stats file name not provided.")

    
    

    if(os.path.isfile(file_name)):
        
        with open(file_name,encoding='utf-8') as f:
            file_content = f.read()
        
        words = file_content.split()
        clean_words = [filter_string(word) for word in words]
        #file_content = [x.strip() for x in file_content] 

        words_dictionary = number_words(clean_words)
        alpha_dictionary = alpha_count(clean_words)
		
        total_words = sum(freq['Frequency'] for freq in words_dictionary.values() if freq) 
        result += '\nTotal words:{tot}'.format(tot=total_words)
		
        for key in sorted(alpha_dictionary.items(), key=lambda item:item[1],reverse=True):
            result += '\n Alphabet "{k}" found {v} times'.format(k=key[0],v=key[1])
        
        result += f"\n\n Total number of unique words are {len(words_dictionary)} \n\n"
		
        for k,v in list(sorted_dictionary.items())[:5]:
            result += '\n word "{w}" found {c} times'.format(w=k,c=v['Frequency'])
            next_word = dict((k, v[k]) for k in v.keys() if k != 'Frequency')
            next_word = [(k, next_word[k]) for k in sorted(next_word, key=next_word.get, reverse=True)]
           
            for key, value in next_word[:3]:
                result += '\n\t {k} : {v}'.format(k=key,v=value)

    if(output): 
	    output_file(out_file,result)
    else: print(f"output file not provided \n {result}")