#!/bin/python3

import math
import os
import random
import re
import sys
import zipfile
os.environ['NLTK_DATA'] = os.getcwd()+"/nltk_data"
import nltk
#
# Complete the 'calculateCFD' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY cfdconditions
#  2. STRING_ARRAY cfdevents
#
from nltk.corpus import brown, stopwords


def calculateCFD(cfdconditions, cfdevents):
    # Write your code here
    #Taks1
    #Determine the conditional frequency of all words
    #store results in sdev_cfd
    
    cfd = nltk.ConditionalFreqDist([
        (genre, word.lower())
         for genre in cfdconditions
          for word in brown.words(categories=genre)])

    cfd.tabulate(conditions = cfdconditions, samples = cfdevents)
    
    cdev_cfd = set(stopwords.words('english'))
    
    #Task 2?
    #Determine the word ending with ing or ed
    
    temp_genre = [(genre, word.lower()) for genre in brown.categories() for word in brown.words(categories=genre) if (word.lower().endswith('ing') or word.lower().endswith('ed'))]
    
    generc_word_list = [list(x) for x in temp_genre]
    
    for wd in generc_word_list:
        if wd[1].endswith('ing') and wd[1] not in cdev_cfd:
            wd[1]= 'ing'
        elif wd[1].endswith('ed') and wd[1] not in cdev_cfd:
            wd[1]= 'ed'
            
    inged_cfd = nltk.ConditionalFreqDist(generc_word_list)
    inged_cfd.tabulate(conditions = cfdconditions, samples = ['ed','ing'])
if __name__ == '__main__':
    cfdconditions_count = int(input().strip())

    cfdconditions = []

    for _ in range(cfdconditions_count):
        cfdconditions_item = input()
        cfdconditions.append(cfdconditions_item)

    cfdevents_count = int(input().strip())

    cfdevents = []

    for _ in range(cfdevents_count):
        cfdevents_item = input()
        cfdevents.append(cfdevents_item)

    if not os.path.exists(os.getcwd() + "/nltk_data"):
        with zipfile.ZipFile("nltk_data.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())

    calculateCFD(cfdconditions, cfdevents)
