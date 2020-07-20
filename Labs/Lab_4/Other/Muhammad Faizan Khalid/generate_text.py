#!/usr/bin/python3
import os
import sys
import random
from text_stat_modified import *

if __name__ == '__main__':
    file_name = None
    inital_words = None
    words_maximum = None


    if(len(sys.argv)==4):

        file_name = sys.argv[1]
        inital_words = sys.argv[2]
        words_maximum = int(sys.argv[3])

        if(os.path.isfile(file_name) and words_maximum > 0 and inital_words.isalpha()):

            with open(file_name,encoding='utf-8') as f:
                content = f.read()
            words = content.split()
            clean_words = [filter_string(word) for word in words]

            dictionary = number_words(clean_words)
            messages = [inital_words]
            
            while words_maximum != 0:
                if(inital_words in dictionary):
                    dict_msgs = dictionary[inital_words]
                    dict_msgs = dict((k, dict_msgs[k]) for k in dict_msgs.keys() if k != 'Frequency')
                    dict_msgs =  [(k, dict_msgs[k]) for k in sorted(dict_msgs, key=dict_msgs.get, reverse=True)]

                    if len(dict_msgs)>0:
                        chosen = [key for key in dict(dict_msgs).keys()]
                        val_msg = [val for val in dict(dict_msgs).values()]
                        val_msg = list(map(int, val_msg))
                        total = int(sum(dict(dict_msgs).values()))
                        probability = [value / total for value in val_msg]

                        rand_choice = random.choices(chosen, weights=probability)
                        messages.append(rand_choice[0])
                        inital_words = rand_choice[0]
                        words_maximum -= 1
                    else:
                        break
                else:
                    break
                
              


            
            messages = ' '.join(messages)
            print(messages)
            
        else:
            print("Invalid parameters, Please prove a valid filename, a valid word and a positive size(number)")

    else:
        print("Please provide a valid filename")