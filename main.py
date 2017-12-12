import re
from ntlk.copus import stopwords


def main():
    search_string = str(input("Please enter the question: "))
    search_words = re.sub("[,?]", '', search_string).split(' ')

    # IDENTIFY IMPORTANT WORDS



   #

def identify_important_words(all_words):
    stopwords_eng = set(stopwords.words('english'))
    return filter(lambda word: not word in stopwords_eng, allWords) 



if "__main__":
    main()
