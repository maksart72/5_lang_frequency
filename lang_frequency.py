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
            value = word_frequence[key]
            word_frequence[key]=value+1
        else:
            word_frequence[key]=1
    
    sorted_keys = sorted(word_frequence, key=lambda x: int(word_frequence[x]), reverse=True)
    return(sorted_keys)

if __name__ == '__main__':
    raw_text = load_raw_text(filepath)
    frequent_words = get_most_frequent_words(raw_text)
    i = 0
    while i<=9:
        s = str(frequent_words[i])
        print(s)
        i = i + 1
