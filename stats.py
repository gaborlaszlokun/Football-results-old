# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 12:10:58 2017

@author: ASUS
"""

import pandas as pd
import os


def make_letter_list(result):
    result_letters = ""
    for i in range(len(result)):
        result_letters += result.iat[i,7]
    letter_arr = result_letters.split("D")
    return letter_arr

def get_last_period(filename):
    result = pd.read_csv(filename)
    letter_arr = make_letter_list(result)
    return len(letter_arr[-1])

def get_max_period(filename):
   result = pd.read_csv(filename)
   letter_arr = make_letter_list(result)
   period_lens = []
   for period in letter_arr:
       period_lens.append(len(period))
   return max(period_lens)

def get_active_stats():
    for folder in os.listdir("active"):
        for file in os.listdir("active/" + str(folder)):
            filename = "active/" + str(folder) + "/" + str(file)
            print folder, get_max_period(filename), get_last_period(filename)
            
#TODO: max betweens
#def get_archive_stats():
            