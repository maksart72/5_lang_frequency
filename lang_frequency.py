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
    most_frequent = [word for word in Counter(vocabluary).most_common(top)]
    return most_frequent

def print_results(most_frequent):
    for word in most_frequent:
        print(word[0],' - founded ',word[1],' times')

if __name__ == '__main__':
    filename = sys.argv[1]
    how_many_words = 10
    result = find_most_frequent_words(load_file(filename), how_many_words)
    print_results(result)
    