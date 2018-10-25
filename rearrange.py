import random
import sys

def rearrange_words():
    user_words = sys.argv[1:] #All arguments from terminal EXCEPT [0] = file name
    words = []
    for word in user_words:
        rando = random.randint(0, len(user_words) - 1)
        remix = user_words[rando]
        words.append(remix)
        show = " ".join(words)
    return show

if __name__ == '__main__':
    rearranged = rearrange_words()
    print(rearranged)
