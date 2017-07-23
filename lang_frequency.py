import sys
import re
import os
from collections import Counter


def load_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file: 
        return file.read()

def find_most_frequent_words(raw_text, top):
    vocabluary = re.findall(r'\w+', raw_text.lower())
    most_frequent = Counter(vocabluary).most_common(top)
    return most_frequent

def print_results(most_frequent):
    for word in most_frequent:
        print(word[0], ' - founded ', word[1], ' times')

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        if not os.path.exists(filename) == True:
            raise Exception ("Error: File doesn't exist!")
    except IndexError:
        print("Error: Empty argument try lang_frequency.py <filename>")
    else:
        how_many_words = 10
        list_most_frequent = find_most_frequent_words(load_file(filename), how_many_words)
        print_results(list_most_frequent)
    