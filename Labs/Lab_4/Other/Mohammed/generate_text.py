#!/usr/bin/env python3
import sys
import random
import text_stats as txtST

temp_previously_used_words = {}


def print_random_word_text(start_word,max_count):
    global temp_previously_used_words

    temp_previously_used_words = {}  # Clear Global Variable
    iteration = 0
    generated_text = start_word
    next_word = start_word

    while int(max_count) > iteration:
        new_word = get_random_word_from_followed_word_list(next_word)
        if new_word == None:
            break
        generated_text = generated_text + ' ' + new_word
        next_word = new_word
        iteration = iteration + 1
    print(generated_text)

def check_cache_data(word):
    global temp_previously_used_words
    if temp_previously_used_words.get(word, None) == None:
        None
    else:
        return temp_previously_used_words[word]

def get_random_word_from_followed_word_list(word):
    global temp_previously_used_words

    if check_cache_data(word) == None:
        follow_words = txtST.follow_word_dic[word]
        if len(follow_words) > 0:
            follow_words_seq = []
            for fword, ftimes in sorted(follow_words.items(), key=lambda item: item[1],reverse = True):
                follow_word_list = [fword] * ftimes
                follow_words_seq.extend(follow_word_list)
            random_index = random.randint(0,len(follow_words_seq) - 1)
            temp_previously_used_words[word] = follow_words_seq # update global variable
            return follow_words_seq[random_index]
        else:
            return None
    else:
        follow_words_seq = check_cache_data(word)
        random_index = random.randint(0,len(follow_words_seq) - 1)
        temp_previously_used_words[word] = follow_words_seq # update global variable
        return follow_words_seq[random_index]



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    if len(sys.argv) == 4:

        contents = txtST.get_file_text(sys.argv[1])
        contents = txtST.get_text_without_special_char(contents)

        print(f'{bcolors.OKBLUE}Please Wait! Generating text results .... .... ... .. .{bcolors.ENDC}')
        print('\n')

        txtST.generate_text_stat(contents)


        print_random_word_text(sys.argv[2],sys.argv[3])
        print('\n')
        print(f'{bcolors.OKGREEN}***Please Note that word with s implie for is word.{bcolors.ENDC}')
        print('\n')
        #open_file(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("Please Provide the (1)File name, (2)Starting Word and (3)Max number of words !")


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main()
    elif len(sys.argv) >= 5:
        print("Please Provide the (1)File name, (2)Starting Word and (3)Max number of words !. No need for extra arguments!")
    else:
        print("Please Provide the File!")


#### References

# https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string