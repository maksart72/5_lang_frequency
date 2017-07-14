import sys
import re
import os


def load_raw_text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler

def get_most_frequent_words(raw_text):
    voc = re.findall(r'\w+', raw_text)
    word_frequence = {}
    for key in voc:
        key = key.lower()
        if key in word_frequence:
            frequence = word_frequence[key]
            word_frequence[key] = frequence + 1
        else:
            word_frequence[key] = 1
    sorted_keys = sorted(word_frequence, key=lambda x: int(word_frequence[x]), reverse = True)
    return sorted_keys

if __name__ == '__main__':
    filename = sys.argv[1]
    rawtext = load_raw_text(filename)
    freqwords = get_most_frequent_words(rawtext)
    keyword = 0
    while keyword <= 9:
        top = str(freqwords[keyword])
        print(top)
        keyword = keyword + 1
