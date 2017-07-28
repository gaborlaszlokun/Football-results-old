# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results
from league_link_collector import sort_links

t = open("archive_links.txt", "r") 
links = t.read()
t.close()

links = links.split("\n")


#for i in range(3334,len(links)):
#    get_results(links[i],"archive")
#    print i
 
sort_links()   
#check_file(links) 

#url = "http://www.worldfootball.net/all_matches/alb-kategoria-superiore-2016-2017/"
#get_results(url)