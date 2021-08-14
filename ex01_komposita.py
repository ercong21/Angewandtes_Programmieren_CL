#!/usr/bin/python3

import sys
from collections import defaultdict
import math

class CompSplitt():
    def __init__(self,filename):
        self.word_freq, self.noun_list = self.read_data(filename)


    def read_data(self,filename):
        """
        :param filename: the data file
        :return: a word frequency dictionary and a set of all nouns
        """
        word_freq = defaultdict(int)
        nouns = set()

        with open(filename,'r',encoding='utf-8') as f:
            for line in f:
                word, label, _ = line.split('\t')
                word = word.lower()
                if label == 'NN' and word.isalpha():
                    word_freq[word] += 1
                    nouns.add(word)

            return word_freq, nouns

    def split(self,word,subwords,s=0):
        l = len(word)
        for e in range(s+3,l+1):  # only subwords of length equal to or more than 3
            subword = word[s:e]
            if subword in self.word_freq:
                update_subwords = subwords + [subword.capitalize()]
                if e == l:
                    yield update_subwords
                else:
                    yield from self.split(word,update_subwords,e)
                    if word[e] == 's':
                        yield from self.split(word,update_subwords,e+1)

    def evaluate_split(self,split):
        product = math.prod(self.word_freq[word.lower()] for word in split)
        score = round(pow(product,1/len(split)),1)
        return score

    def print_result(self):
        for word in sorted(self.noun_list):
            best_score = 0
            best_split = [word]
            for split_result in self.split(word,list()):
                score = self.evaluate_split(split_result)
                if score > best_score:
                    best_score = score
                    best_split = split_result
            print(word.capitalize(), best_score, *best_split)

def main():
    data_file = sys.argv[1]
    comp_split = CompSplitt(data_file)
    comp_split.print_result()

if __name__ == '__main__':
    main()





