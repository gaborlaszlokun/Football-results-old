# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:23:02 2017

@author: ASUS
"""

import pandas as pd
import os

for folder in os.listdir("archive_"):
    for file in os.listdir("archive_/" + str(folder)):
        filename = "archive_/" + str(folder) + "/" + str(file)
        if ".csv" in filename:
            print filename
            results = pd.read_csv(filename)
            results['Date'] =pd.to_datetime(results['Date'], dayfirst = [True])
            results = results.sort_values(['Date', 'Time'], ascending=[True, True])
#            print results
            results.to_csv(filename, sep=',', encoding='utf-8', index=False)