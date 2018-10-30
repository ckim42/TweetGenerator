import sys

def histogram():
    f = open(sys.argv[1], "r").read().split()
    words = []
    for word in f:
        if word not in words:
            words.append([word, 1])
        for i in words:
            if i[0] == word:
                i[1] += 1
    return words

print(histogram())

#Thanks to Dylan Finn
