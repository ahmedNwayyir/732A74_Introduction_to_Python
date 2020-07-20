 #! /usr/bin/env python3
import sys

def error_handle():
    if len(sys.argv) ==1:
        print("You have not provided any file!")
        return False

    import os.path
    if os.path.isfile(sys.argv[1]):
        return True
    else:
        print("The file does not exist!")
        return False


def text_filter(mytext):
    text_words = {}
    words_list = [word.lower() for word in mytext.split()]
    bad_chars = [".", "?", ":", ";", "'", ",", "!", "[", "]", "_"]
    for i in range(len(words_list)):
        for char in words_list[i]:
            if char in bad_chars:
                #if char == words_list[i][-1]:
                words_list[i] = words_list[i].replace(char, "")

    words = list(filter(lambda w:w != ".", words_list))
    return(words)


def data_base(mytext):
    words = text_filter(mytext)
    db={'alphabets':{}, 'text_words':{},'frequents':[], 'unique':0, 'number_of_words':0}

    for word in words:
        if word in db['text_words'].keys():
            db['text_words'][word] +=1
        else:
            db['text_words'][word] = 1

        for char in word:

            if char.isalpha():
                if char in db['alphabets'].keys():

                    db['alphabets'][char] +=1
                else:
                    db['alphabets'][char] = 1

    db['number_of_words'] = sum(db['text_words'].values())
    #sorting the alphabets
    db['alphabets'] = sorted(db['alphabets'].items(), key = lambda kv: kv[0])
    #Top 5 words
    sort_words = sorted(db['text_words'].items(), key= lambda kv: kv[1], reverse=True)
    db['frequents'] = (sort_words[0:5])

    #unique words
    db['unique'] = len(set(db['text_words'].keys()))

    #top 3 successors which follow the 5 most frequent words
    top_five = [top[0] for top in db['frequents']]
    db['successors'] = {top:{} for top in top_five}
    for word in top_five:
        for i in range(len(words)):
            if word == words[i]:
                if words[i+1] in db['successors'][word].keys():
                    db['successors'][word][words[i+1]] +=1
                else:
                    db['successors'][word][words[i+1]] = 1
    for k in db['successors'].keys():
        db['successors'][k] = sorted(db['successors'][k].items(), key=lambda kv:kv[1], reverse=True)


    return(db)




# Writing the result in the output file. "frequency" is a user selected number to return the words repeated in the text with that frequency.
def output(mytext):
    db = data_base(mytext)

    if len(sys.argv) > 2:
        with open(sys.argv[2], encoding="utf-8", mode="w+") as out:

            out.write("The result of file survey is as follow:\n")
            out.write("******\n\n")
            out.write(f"The total number of words in the text is {db['number_of_words']}\n")

            out.write("*************************************************************************\n")

            out.write(f"The 5 most frequent words are:\n")
            for word in db['frequents']:
                out.write(word[0]+'\t'+ str(word[1])+'\n')


            out.write("\n************************************************************************\n")
            out.write("The 3 top successors of the 5 most frequent words:\n")
            for k in range(len(db['successors'].keys())):
                out.write("--------------------------\n")
                out.write(db["frequents"][k][0] + '('+str(db["frequents"][k][1])+ 'occurrences)'+'\n')
                for v in db['successors'][db["frequents"][k][0]][0:3]:
                    out.write(f'--{v[0]},\t {v[1]}\n')

            out.write('\n************************************************************************\n')
            out.write("The occurences of alphabets are as follow:\n")
            for i in range(len(db['alphabets'])):
                out.write(db['alphabets'][i][0]+ '\t' + str(db['alphabets'][i][1]) + '\n')


            out.write('\n************************************************************************\n')
            out.write(f"The unique words:")
            out.write(str(db['unique']))



    else:

        print("The result of file survey is as follow:\n")
        print("******\n\n")
        print(f"The total number of words in the text is {db['number_of_words']}\n")
        print("*************************************************************************\n")

        print(f"The 5 most frequent words are:\n")
        for word in db['frequents']:
            print(word[0]+'\t'+ str(word[1])+'\n')


        print("\n************************************************************************\n")
        print("The 3 top successors of the 5 most frequent words:\n")
        for k in range(len(db['successors'].keys())):
            print("--------------------------\n")
            print(f'{db["frequents"][k][0]} ({db["frequents"][k][1]} occurrences)\n')
            for v in db['successors'][db["frequents"][k][0]][0:3]:
                print(f'--{v[0]},\t {v[1]}\n')

        print('\n************************************************************************\n')
        print("The occurences of alphabets are as follow:\n")
        for i in range(len(db['alphabets'])):
            print(f"{db['alphabets'][i][0]} \t {db['alphabets'][i][1]}\n")


        print('\n************************************************************************\n')
        print(f"The unique words: {db['unique']}")



def main():
    if error_handle():
        with open(sys.argv[1], encoding="utf-8", mode="r") as file1:
            myText = file1.read()
            output(myText)


if __name__ == "__main__":
    main()
