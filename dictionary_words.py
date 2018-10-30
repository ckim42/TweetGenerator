import random
import sys

def load_word():
    words = []
    i = 0
    length = int(sys.argv[1])
    while i < length:
        f = open('words.txt', 'r').read().split()
        word = random.choice(f)
        words.append(word)
        show = " ".join(words)
        i += 1
    return show

if __name__ == '__main__':
    scattered = load_word()
    print(scattered)

#Thanks to Dylan Finn, Anwar Azeez, & Erica Naglik
