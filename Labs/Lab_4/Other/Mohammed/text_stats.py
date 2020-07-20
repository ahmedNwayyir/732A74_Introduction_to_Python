#!/usr/bin/env python3
import sys
import re as regX

letter_dic = {}
word_dic = {}
follow_word_dic = {}


def get_file_text(fname):

    try:
        f = open(fname,"r")
    except OSError:
        print(f"{bcolors.FAIL}The file does not exist! Could not open/read file: {fname}{bcolors.ENDC}")

    with f:
        contents = f.read()
        f.close()
        return contents

def get_text_without_special_char(wordset):

    lower_cased = wordset.lower()
    special_char_removed_text = regX.sub(r'[^a-zA-ZäöåÄÖÅ]', ' ', lower_cased)
    return(special_char_removed_text)

def get_words_list(wordset):
    bookwords = wordset.split()
    return(bookwords)

def get_all_followed_words(word,textList):
    follow_words = [textList[index + 1] for index in range(len(textList)) if textList[index]==word and index + 1 < len(textList)]

    word_count = {}

    for word in follow_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def generate_text_stat(wordset):
    global word_dic

    lower_cased = wordset.lower()
    bookwords = lower_cased.split()

    pre_word = None
    cur_word = None

    for w in bookwords:
        pre_word = cur_word
        cur_word = w
        update_letter_frequencey(w)
        if pre_word is not None and cur_word is not None:
            update_follow_word(pre_word,cur_word)

        if w in word_dic:
            word_dic[w] += 1
        else:
            word_dic[w] = 1

def update_letter_frequencey(word):
    global letter_dic

    word_letters = list(word)

    for letter in word_letters:
        if letter in letter_dic:
            letter_dic[letter] += 1
        else:
            letter_dic[letter] = 1

def update_follow_word(pre,cur):
    global follow_word_dic

    if pre in follow_word_dic:
        temp_follow_list = follow_word_dic[pre]
        if cur in temp_follow_list:
            temp_follow_list[cur] += 1
        else:
            temp_follow_list[cur] = 1
    else:
        follow_word_dic[pre] = {f'{cur}': 1}

def get_top_items(headCount,data_list):
    counter = 1
    headItems = {}
    for word, times in sorted(data_list.items(), key=lambda item: item[1],reverse = True):
        if counter <= headCount:
            headItems[word] = times
            counter = counter + 1
    return headItems

def print_most_freq_words_and_follow_word(freqWordCount,followUpWordCount):
    global word_dic
    global follow_word_dic

    print(f"{bcolors.OKGREEN}Most {freqWordCount} Frequent words and it's {followUpWordCount} most common follow words :-{bcolors.ENDC}")
    top_words_list = get_top_items(freqWordCount,word_dic)
    for word, times in sorted(top_words_list.items(), key=lambda item: item[1],reverse = True):
        print(f"{word} ( {times} occurences )")
        follow_words = get_top_items(followUpWordCount,follow_word_dic[word])
        for fword, ftimes in sorted(follow_words.items(), key=lambda item: item[1],reverse = True):
            print(f"-- {fword}, {ftimes}")


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
    contents = get_file_text(sys.argv[1])
    contents = get_text_without_special_char(contents)
    text_word_count = len(get_words_list(contents))

    print(f'{bcolors.OKBLUE}Please Wait! Generating text results ....{bcolors.ENDC}')
    print('\n')

    generate_text_stat(contents)

    print("Text Letter Frequency :-")
    for letter, times in sorted(letter_dic.items(), key=lambda item: item[1],reverse = True):
        print(f"{letter} was found {times} times")

    print('\n')

    print(f"{bcolors.OKGREEN}Text Total Word Count is {text_word_count}{bcolors.ENDC}")
    print('\n')

    print(f"{bcolors.OKGREEN}Text Unique Word Count is {len(word_dic)}{bcolors.ENDC}")
    print('\n')

    print_most_freq_words_and_follow_word(5,3)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    elif len(sys.argv) >= 3:
        print("Please provide file name only. No need for extra arguments!")
    else:
        print("Please Provide the File!")

#### References

# https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string