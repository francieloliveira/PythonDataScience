#!/bin/python3

import math
import os
import random
import re
import sys
import zipfile
os.environ['NLTK_DATA'] = os.getcwd() + "/nltk_data"
import nltk
from urllib import request
#
# Complete the 'processRawText' function below.
#
# The function accepts STRING textURL as parameter.
#

def processRawText(textURL):
    textcontent = request.urlopen(textURL).read().decode('utf8')
    tokens = nltk.tokenize.word_tokenize(textcontent)
    tokenizedlcwords = [x.lower() for x in tokens]
    noofwords = len(tokenizedlcwords)
    settokenslcwords = set(tokenizedlcwords)
    noofunqwords = len(settokenslcwords)
    wordcov = int(noofwords / noofunqwords)
    count = 0
    wordfreq = {}
    for x in tokenizedlcwords:
        if str(x).isalpha():
            t = []
            t.append((x, tokenizedlcwords.count(x)))
            wordfreq.update(t)
    maxfreq = max(wordfreq, key=wordfreq.get)
    return noofwords, noofunqwords, wordcov, maxfreq
    
    
    
if __name__ == '__main__':
    textURL = input()

    if not os.path.exists(os.getcwd() + "/nltk_data"):
        with zipfile.ZipFile("nltk_data.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())

    noofwords, noofunqwords, wordcov, maxfreq = processRawText(textURL)
    print(noofwords)
    print(noofunqwords)
    print(wordcov)
    print(maxfreq)
