'''
This script runs a frequency analysis for words in a given text. It returns top 10 most frequent words and they appearance frequancy.

Usage: lang_frequancy.py [filename]

Anton Demkin, 2017
antondemkin@yandex.ru
'''

# import regular expressions
import re
# module needed for sorting. Dunno what it is.
import operator
import sys
import os


def load_data(filepath):
    '''
    Load a text file and return in like a string
    '''
    big_text = ''
    with open(filepath) as text:
        for line in text:
            big_text += line
    return big_text


def filter_string(string):
    '''
    Return a string without any special symbols and lower case only.
    '''
    # remove all special symbols
    s = re.sub("[^A-Za-z0-9']+", " ", string)
    # convert to lower case
    s = s.lower()
    return s


def get_most_frequent_words(string):
    '''
    Return a dict with all words and word count.
    '''
    # separate words by spaces
    text = string
    words = text.split()
    word_counter = {}
    for word in words:
        # create key if word never seen before
        if word not in word_counter:
            word_counter[word] = 1
        # increase key count if word already in dict
        elif word in word_counter:
            word_counter[word] += 1
    
    return word_counter


def top_results(word_dict, filename, number_of_top_results=10):
    '''
    Prints most frequently seen words in a given words dictionary.
    '''
    
    # sort dict keys by item
    sorted_result = sorted(word_dict.items(), key=operator.itemgetter(1))
    sorted_result.reverse()
    # print top results
    print("Frequency analysis for %s:" % filename)
    for i in range(number_of_top_results):
        if sorted_result[i]:
            print("%s: %d" % (sorted_result[i][0], sorted_result[i][1]))


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1:]
        file = file[0]
        path = os.path.join(os.getcwd(), file)
        # print(file)
        text = load_data(path)
        text = filter_string(text)
        result = get_most_frequent_words(text)
        top_results(result, file, 10)
    else:
        print("Usage: lang_frequency.py [text file]")


if __name__ == '__main__':
    main()
