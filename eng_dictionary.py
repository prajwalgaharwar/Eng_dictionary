#!/usr/bin/env python
# coding: utf-8

import json
from difflib import get_close_matches
data=json.load(open("data.json",'r'))
words= data.keys()

def getWord(word):
    if word in data:
        return data[word]
    else:
        return 0

word=input("Enter a word: ").lower()
meaning = getWord(word)

if type(meaning)==list:
    print("\n {} means:".format(word.capitalize()))
    for a in range(len(meaning)):
        print("{}. {}".format(a+1,meaning[a]))
else:
    match=get_close_matches(word,words,cutoff=0.8)
    if len(match)>0:
        mth_ip =input("Did you mean {} ? Enter Y for yes and N for no]? ".format(match[0]))
        if mth_ip.lower()== 'y':
            meaning = getWord(match[0])
            if type(meaning)==list:
                print("\n {} means:".format(match[0].capitalize()))
                for a in range(len(meaning)):
                    print("{}. {}".format(a+1,meaning[a]))
        elif mth_ip.lower()== 'n':
            print("The word entered does not exist. Please check the input")            
    else:
        print("The word entered does not exist. Please check the input")







