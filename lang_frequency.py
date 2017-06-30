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


def top_results(word_dict, filename, how_many=10, detailed=True):
    '''
    Prints most frequently seen words in a given words dictionary.
    :keyword word_dict: dictionary
    :keyword filename: name of the file, only for readability purpose.
    :keyword how_many: how many top results you want to print
    :keyword detailed: prints how many times words has been seen if true. Only words if false.
    '''
    
    # sort dict keys by item
    result = sorted(word_dict.items(), key=operator.itemgetter(1))
    result.reverse()
    # print top results
    print("Frequency analysis for %s:" % filename)
    for i in range(how_many):
        if result[i]:
            if detailed:
                print("%s: %d" % (result[i][0], result[i][1]))
            else:
                print("%s" % result[i][0])


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1:]
        path = path[0]
        if os.path.exists(path) == False:
            # convert filename to path if launched with filename.txt without path
            path = os.path.join(os.getcwd(), path)
        # if launched with full path, go straight to analysis.
        # load file into string
        text = load_data(path)
        # filter string
        text = filter_string(text)
        # count words
        result = get_most_frequent_words(text)
        # print results
        top_results(result, path, 10, False)
    else:
        print("Usage: lang_frequency.py [text file or path]")


if __name__ == '__main__':
    main()
