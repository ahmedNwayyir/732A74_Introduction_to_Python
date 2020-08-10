#!/usr/bin/env python3
import sys, os, re, itertools
from collections import Counter


def preProcess(file):
    contents = file.read().lower()
    pattern = re.compile(r'[a-zàæèäöåÄÖÅ]+')
    words = pattern.findall(contents)
    return words


def countLetters(contents):
    contents = ' '.join(contents)
    letters_dic = {}
    for letter in set(contents): 
        letters_dic[letter] = contents.count(letter)
    letters_dic = sorted(letters_dic.items(), key=lambda x: x[1], reverse=True)[1:]
    return letters_dic


def countWords(contents):
    return len(contents)


def countUniqueWords(contents):
    unique_words = set(contents)
    return len(unique_words)


def getCommonWords(contents):
    common_words = Counter(contents)
    common_words = sorted(common_words.items(), key=lambda x: x[1], reverse=True)
    return common_words


def getWordPairs(contents):
    copy1, copy2 = itertools.tee(contents)
    next(copy2, None)
    word_pairs = Counter((word1, word2) for word1, word2 in zip(copy1, copy2))
    return word_pairs

def getFollowWords(common_words, word_pairs):
    common_words = [a_tuple[0] for a_tuple in common_words[0:5]]
    follow_words = {}
    for word in common_words:
        word_dic = {pair:count for pair, count in word_pairs.items() if pair[0] == word}
        word_dic = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)[0:3]
        follow_words[word] = [word_dic[0][0][1], word_dic[0][1], word_dic[1][0][1], word_dic[1][1], word_dic[2][0][1], word_dic[2][1]] 
    return follow_words    


def output(contents):
    print("Text Statististcs for Shakespeare.txt\n")
    sep = "*" * 40 + "\n\n"
    print(sep)

    print(f'Total number of words :{countWords(contents):,}\n')
    print(sep)

    print(f'\nNumber of unique words :{countUniqueWords(contents):,}\n')
    print(sep)

    print("\nCommon Words:\n")
    print(sep)
    common_words = getCommonWords(contents)[0:5]
    for word in common_words:
        print(word[0]+ '\t' + str(word[1]) + '\n')

    print("\n\nLetter frequency:\n")
    print(sep)
    letter_counts = countLetters(contents)
    for letter_count in letter_counts:
        print(letter_count[0]+ '\t' + str(letter_count[1]) + '\n')

    print("\n\nMost common following words:\n")
    print(sep)
    word_pairs = getWordPairs(contents)
    follow_words = getFollowWords(common_words, word_pairs)
    for key, value in follow_words.items():
        print(f"{key} \n\t {value[0:2]} \n\t {value[2:4]} \n\t {value[4:6]}\n")


def writeToFile(contents):
    common_words = getCommonWords(contents)
    with open(sys.argv[2], "a", encoding="utf-8") as out:
        out.write("Text Statististcs for Shakespeare.txt\n")
        sep = "*" * 40 + "\n\n"
        out.write(sep)

        out.write(f'Total number of words :{countWords(contents):,}\n')
        out.write(sep)

        out.write(f'\nNumber of unique words :{countUniqueWords(contents):,}\n')
        out.write(sep)

        out.write("\nCommon Words:\n")
        out.write(sep)
        common_words = getCommonWords(contents)[0:5]
        for word in common_words:
            out.write(word[0]+ '\t' + str(word[1]) + '\n')

        out.write("\n\nLetter frequency:\n")
        out.write(sep)
        letter_counts = countLetters(contents)
        for letter_count in letter_counts:
            out.write(letter_count[0]+ '\t' + str(letter_count[1]) + '\n')

        out.write("\n\nMost common following words:\n")
        out.write(sep)
        word_pairs = getWordPairs(contents)
        follow_words = getFollowWords(common_words, word_pairs)
        for key, value in follow_words.items():
            out.write(f"{key} \n\t {value[0:2]} \n\t {value[2:4]} \n\t {value[4:6]}\n")


def main():
    if len(sys.argv) < 2:
        print("No read file provided!")
        sys.exit(1)    

    elif not os.path.isfile(sys.argv[1]):
        print(f"The file {sys.argv[1]} does not exist!")
        sys.exit(1)

    elif os.path.isfile(sys.argv[1]):      
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            contents = preProcess(file) 
            output(contents)
        if len(sys.argv) > 2:
            writeToFile(contents)


if __name__ == '__main__':
    main()