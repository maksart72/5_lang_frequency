import sys, re

filepath = sys.argv[1]

def load_text(filepath):
    fo = open(filepath,'r')
    text = fo.read()
    fo.close()
    return(text)

def get_most_frequent_words(text):
    voc = re.findall(r'\w+',text)
    
    lsWord = {}
    for key in voc:
        key = key.lower()
        if key in lsWord:
            value = lsWord[key]
            lsWord[key]=value+1
        else:
            lsWord[key]=1
    
    sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
    return(sorted_keys)

if __name__ == '__main__':
    text = load_text(filepath)
    frequent_words = get_most_frequent_words(text)
    i = 0
    while i<=9:
        s = str(frequent_words[i])
        print(s)
        i = i + 1
