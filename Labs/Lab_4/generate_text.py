#!/usr/bin/env python3
import sys, text_stats
from random import choices


def textGenerator(contents):
    cur_word = sys.argv[2]
    max_words = int(sys.argv[3])

    msg = cur_word

    word_pairs = text_stats.getWordPairs(contents)
    word_dic = {pair[1]:count for pair, count in word_pairs.items() if pair[0] == cur_word}
    word_count = sum(word_dic.values())

    word_counter = 1
    while word_counter < max_words and len(list(word_dic.keys())) > 0:
        next_weights = {next_word:count/word_count for next_word, count in word_dic.items()}
        next_word = choices(population=list(next_weights.keys()), weights=list(next_weights.values()), k=1)
        cur_word = next_word[0]
        msg = msg + " " + cur_word
        del word_dic[cur_word]
        word_counter += 1
    
    return msg  


def main():
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        contents = text_stats.preProcess(file)
    text = textGenerator(contents)
    print(text)


if __name__ == '__main__':
    main()

