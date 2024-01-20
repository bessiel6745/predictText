# -*- coding: utf-8 -*-
"""
Authors: Bessie Li
Consulted:
Date: 11/15/23
Purpose: predictText task: Based on observed words, predict the next
    word that will be typed.
"""

import random


#-----------------------------#
# Provided code (DO NOT EDIT) #
#-----------------------------#

def chooseRandomly(options):
    """
    Accepts a sequence of options and returns a random option from that
    sequence. Note: you MUST use this function to pick random words in
    your code below, otherwise your assignment will not be graded
    properly."""
    return random.choice(list(options))


#----------------------#
# Write your code here #
#----------------------#

def buildPredictions(list):
    """this function returns a dictionary by adding values to keys"""
    dict = {}
    for i in range(len(list)-1):
        word = list[i].lower()
        word1 = list[i+1].lower()
        if word not in dict:
            dict[word] = []
        dict[word].append(word1)
    if len(dict)>= 2:
        return dict
    return {}

def nextWord(current, dict, default):
    """this function returns a random value in a dictionary if the key is in it"""
    if current.lower() in dict:
        x = chooseRandomly(dict[current])
        return x
    return default

def predictText(startWord, howMany, predictions):
    """this function returns a list of the start word and then it adds values from dictionaries"""
    now = startWord.lower()
    list = [now]
    for i in range(howMany):
        now = nextWord(now, predictions, startWord)
        list.append(now)
    return list


    
    
