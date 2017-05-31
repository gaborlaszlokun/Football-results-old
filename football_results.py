# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results

t = open("league_links.txt", "r") 
links = t.read()
t.close()

t = open("filenames.txt", "r") 
filenames = t.read()
t.close()
links = links.split("\n")
filenames = filenames.split("\n")
for i in range(3096,len(links)):
    get_results(links[i],filenames[i])
    print i
        
#url = "http://www.worldfootball.net/all_matches/alb-kategoria-superiore-2016-2017/"
#get_results(url)