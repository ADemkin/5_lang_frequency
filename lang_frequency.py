'''
This script runs a frequency analysis for words in a given text.
It returns top 10 most frequent words and they appearance frequency.

Usage: lang_frequency.py [path]

Anton Demkin, 2017
antondemkin@yandex.ru
'''


import re
import operator
import sys
import os
import collections


def load_data(filepath):
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
    all_words = text.split()
    # count words
    return collections.Counter(all_words)


def get_top_ten(word_dict):
    
    # sort dict keys by item
    most_frequent_words = sorted(word_dict.items(), key=operator.itemgetter(1))
    most_frequent_words.reverse()
    
    for word in most_frequent_words[:10]:
        yield word[0]


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        text = load_data(path)
        filtered_text = keep_only_lowercase_letters(text)
        top_ten_words = get_most_frequent_words(filtered_text)
        for word in get_top_ten(top_ten_words):
            print(word)
    else:
        print("Usage: lang_frequency.py [path]")


if __name__ == '__main__':
    main()
