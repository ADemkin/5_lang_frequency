import re
import operator
import sys
import os
import collections


def load_data(filepath):
    with open(filepath) as file:
        text = file.read()
    return text


def get_most_frequent_words(string):
    number_of_results = 10
    all_words = string.split()
    return collections.Counter(all_words).most_common(number_of_results)



def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            text = load_data(path)
            # keep only letters, digits and '
            filtered_text = re.sub("[^A-Za-z0-9']+", " ", text)
            lowercase_text = filtered_text.lower()
            top_ten_words_count = get_most_frequent_words(lowercase_text)
            for word in top_ten_words_count:
                print(word[0])


if __name__ == '__main__':
    main()
