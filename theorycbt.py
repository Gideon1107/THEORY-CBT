#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:16:37 2022

@author: gideon
"""

# Answers
# a noun is a name of any person, animal,place or thing
# A pronoun is a word that is used instead of a noun or noun phrase
# a word or phrase that modifies or qualifies an adjective, verb


def cbt_theory():
    score = 0
    question = {1:['what is a noun?'],
                2:['what is a pronoun?'],
                3:['what is an adverb?']}
    
    answer = {1:['name','person','animal','place','thing'],
              2:['word','used','instead','noun','noun phrase'],
              3:['word','modifies','qualifies','adjective','verb']}
    
    for i in question:
        que = question[i]
        print(i,'.',que[0])
        ans = ('Type in your answer: ')
        for i in answer:
            key_word = answer[i]
        if any(i in key_word[0] for i in ans.split()):
            score += 5
        else:
            pass
    print('YOUR TOTAL SCORE IS',score,'.')
cbt_theory()