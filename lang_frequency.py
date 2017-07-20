import sys
import re
import os
from collections import Counter


def load_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return file.read()

def print_most_frequent_words(raw_text, top):
    vocabluary = re.findall(r'\w+', raw_text.lower())
    for word in Counter(vocabluary).most_common(top):
        print(word[0])

if __name__ == '__main__':
    filename = sys.argv[1]
    how_many_words = 10
    print_most_frequent_words(load_file(filename), how_many_words)
