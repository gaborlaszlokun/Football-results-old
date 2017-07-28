# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results, format_filename
from league_link_collector import sort_links


#while True:
t = open("active_links.txt", "r") 
links = t.read()
t.close()

links = links.split("\n")
#
for link in links:
    get_results(link,"active")
    print link
 
#link = "http://www.worldfootball.net/all_matches/irq-super-league-2016-2017/"
#get_results(link,"active")
 
#sort_links()   
#check_file(links) 

#url = "http://www.worldfootball.net/all_matches/alb-kategoria-superiore-2016-2017/"
#get_results(url)