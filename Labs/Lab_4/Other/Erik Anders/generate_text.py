#!/usr/bin/env python3

import sys
import random
import string
import text_stats

def nextword(following):
    f_sum = 0
    for k,v in following.items():
        f_sum = f_sum + v
    
    r_val = random.uniform(0,f_sum) 
    f_sum = 0
    for k,v in following.items():
        f_sum = f_sum + v
        if f_sum > r_val:
            return k
            break


def generator(words, sword, maxwords):
    d = text_stats.followingwords(words)

    
    #algorithm
    cur_word = sword
    msg = cur_word
    w_counter = 1
    while len(d[cur_word].items())>0 and w_counter <= maxwords:
            cur_word = nextword(d[cur_word])
            msg = msg + " " + cur_word
            w_counter = w_counter + 1
    print(msg)

def programm(filename, sword, maxwords):
    
    try: 
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("The file does not exist!")

    else:
        #preprocessing words
        words = contents.split()
        words = [a.lower() for a in words]
        words = [a.translate(str.maketrans('','',string.punctuation)) for a in words]

        generator(words, sword, int(maxwords))









if __name__ == "__main__":
    print("Running as main.")
    if len(sys.argv) <= 3:
        print("Missing arguments!")
    else:
        programm(sys.argv[1], sys.argv[2], sys.argv[3])

else:
    print("I was imported!")