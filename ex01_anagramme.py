#!/usr/bin/env python3
import sys
from collections import defaultdict

with open(sys.argv[1]) as corpus:
    wordlist = {line.split()[0] for line in corpus}  # store vocabulary in a set

anagram_lookup = defaultdict(set)  # 'list of chars':{'set', 'of', 'words'}

for word in wordlist:
    uniq_chars = sorted(word.lower())
    id_str = ''.join(uniq_chars)  # id_str is used to identify all words with the same uniq chars in anagram_lookup
    if id_str.isalpha():
        anagram_lookup[id_str].add(word)

for id, anagrams in anagram_lookup.items():
    if len(anagrams) > 1:
        print(*sorted(anagrams))  # print(*iterator) can print a sequence of elements in an interator divided by space