import sys

def histogram():
    f = open(sys.argv[1], "r").read().split()
    words = []
    for word in f:
        if word not in words:
            words.append((word, f.count(word)));
    return words

print(histogram())

#Thanks to Dylan Finn
