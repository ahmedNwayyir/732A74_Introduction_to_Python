#!/usr/bin/env python3
import sys, text_stats
from random import choices


def textGenerator(contents):
    cur_word = sys.argv[2]
    max_words = int(sys.argv[3])
    msg = cur_word

    pair_counts = text_stats.getPairCounts(contents)
    # get the successive words and their frequencies of the chosen word
    follow_words_dic = {pair[1]:count for pair, count in pair_counts.items() if pair[0] == cur_word}

    word_counter = 0
    # loop through the succussive words of the chosen word 
    while word_counter < max_words and cur_word != [follow_words_dic.keys][-1]:
        # for the current word in the loop we get the frequencies of the succussive words
        follow_words_dic = {pair[1]:count for pair, count in pair_counts.items() if pair[0] == cur_word}
        # randomly pick (based on weight) the next word
        next_word = choices(population= list(follow_words_dic.keys()), weights = list(follow_words_dic.values()), k = 1)
        cur_word = next_word[0]
        msg = msg + " " + cur_word
        word_counter += 1

    return msg  


def main():
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        contents = text_stats.preProcess(file)
    text = textGenerator(contents)
    print(text)


if __name__ == '__main__':
    main()

