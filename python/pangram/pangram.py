from collections import Counter
from string import ascii_lowercase


def is_pangram(sentence):
    counter = Counter(str.lower(letter) for letter in sentence)
    for letter in list(ascii_lowercase):
        if letter not in counter.keys():
            return False
    return True
