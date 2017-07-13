# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results, sort_links, check_file

t = open("archive_links.txt", "r") 
links = t.read()
t.close()

links = links.split("\n")

#get_results("http://www.worldfootball.net/all_matches/aus-a-league-1977/")

for i in range(3334,len(links)):
    get_results(links[i])
    print i
 
#sort_links(links)   
#check_file(links) 

#url = "http://www.worldfootball.net/all_matches/alb-kategoria-superiore-2016-2017/"
#get_results(url)