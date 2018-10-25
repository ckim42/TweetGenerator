import random
import sys

i = 0
location = int(sys.argv[1])
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    split = words_list = words_list[0].split(' ')
    word = random.choice(split)
    return word

while i < location:
    print(load_word())
    i += 1

#Thanks to Anwar Azeez and Erica Naglik
