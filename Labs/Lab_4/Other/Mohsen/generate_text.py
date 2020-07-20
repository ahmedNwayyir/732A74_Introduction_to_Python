import text_stats as ts
import sys
import random


def text_gen(text, word, max):
    myWords = ts.text_filter(text)
    mydict = {}

    for i in range(len(myWords)):
        if word == myWords[i]:
                if myWords[i+1] in mydict.keys():
                    mydict[myWords[i+1]] +=1
                else:
                    mydict[myWords[i+1]] = 1

    mydict = dict(sorted(mydict.items(), key=lambda kv:kv[1], reverse=True))


    total = sum(list(mydict.values()))

    for k,v in mydict.items():
        mydict[k] = round(v/total, 5)

    cur_word = word
    msg = cur_word

    count = 0
    while len(list(mydict.keys())) > 0 and count<int(max):
        cur_word = random.choices(population = list(mydict.keys()), weights=list(mydict.values()), k=1)[0]

        msg = msg + " " + cur_word
        del mydict[cur_word]
        count +=1

    print(msg)




if len(sys.argv) !=4:
    print("You have not provided 3 arguments!")
    sys.exit()

try:
    with open(sys.argv[1], encoding="utf-8", mode="r") as file1:
        myText = file1.read()
        given_word = sys.argv[2]
        max_words = sys.argv[3]
    db = ts.data_base(myText)
    text_gen(myText, given_word, max_words)


except IOError:
    print("The file does not exist!")
