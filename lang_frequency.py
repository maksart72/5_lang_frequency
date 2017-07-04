import sys, re

filepath = sys.argv[1]

def load_raw_text(filepath):
    fo = open(filepath,'r')
    raw_text = fo.read()
    fo.close()
    return(raw_text)

def get_most_frequent_words(raw_text):
    voc = re.findall(r'\w+',raw_text)
    
    word_frequence = {}
    for key in voc:
        key = key.lower()
        if key in word_frequence:
            frequence = word_frequence[key]
            word_frequence[key]=frequence+1
        else:
            word_frequence[key]=1
    
    sorted_keys = sorted(word_frequence, key=lambda x: int(word_frequence[x]), reverse=True)
    return(sorted_keys)

if __name__ == '__main__':
    raw_text = load_raw_text(filepath)
    frequent_words = get_most_frequent_words(raw_text)
    keyword = 0
    while keyword<=9:
        top = str(frequent_words[keyword])
        print(top)
        keyword = keyword + 1
