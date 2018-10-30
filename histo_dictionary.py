import sys
import random

def histogram():
    filename = sys.argv[1]
    f = open(filename, "r").read().split()
    word = random.choice(f)
    dict = {'entry': 0}
    for entry in f:
        dict[entry] = 0
        dict[entry] += 1
    return dict

print(histogram())

# Thanks to Dylan Finn
