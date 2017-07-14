'''
This script runs a frequency analysis for words in a given text.
It returns top 10 most frequent words and they appearance frequency.

Usage: lang_frequency.py [filename]

Anton Demkin, 2017
antondemkin@yandex.ru
'''


import re
import operator
import sys
import os
import collections


def load_data(filepath):
    # (devman) load whole file
    with open(filepath) as file:
        text = file.read()
    return text


def keep_only_lowercase_letters(string):
    # remove all special symbols and convert to lowercase
    text = re.sub("[^A-Za-z0-9']+", " ", string)
    text = text.lower()
    return text


def get_most_frequent_words(string):
    '''
    Return a dict with all words and word count.
    '''
    text = string
    # separate words by spaces
    words = text.split()
    # count words
    return collections.Counter(words)


def print_top_results(word_dict, filename, how_many=10, detailed=True):
    '''
    Prints most frequently seen words in a given words dictionary.
    '''
    
    # sort dict keys by item
    most_frequent_words = sorted(word_dict.items(), key=operator.itemgetter(1))
    most_frequent_words.reverse()
    
    # print top results
    for i in range(how_many):
        if most_frequent_words[i]:
            if detailed:
                print("Frequency analysis for %s:" % filename)
                print("%s: %d" % (most_frequent_words[i][0], most_frequent_words[i][1]))
            else:
                print("%s" % most_frequent_words[i][0])


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            print("%s is not correct path." % str(path))
        else:
            text = load_data(path)
            filtered_text = keep_only_lowercase_letters(text)
            top_ten_words = get_most_frequent_words(filtered_text)
            print_top_results(top_ten_words, path, 10, False)
        
    else:
        print("Usage: lang_frequency.py [text file or path]")


if __name__ == '__main__':
    main()
