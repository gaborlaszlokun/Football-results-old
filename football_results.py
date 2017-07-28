# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results, format_filename
from league_link_collector import sort_links

t = open("active_links.txt", "r") 
links = t.read()
t.close()

links = links.split("\n")

#for link in links:
#    filename = link.replace("http://www.worldfootball.net/all_matches/","").replace("/","")
#    filename = format_filename(filename)
#    print filename
    
#format_filename("mex-primera-division-2017-2018-apertura")

for i in range(0,len(links)):
    get_results(links[i],"active")
    print i
 
#sort_links()   
#check_file(links) 

#url = "http://www.worldfootball.net/all_matches/alb-kategoria-superiore-2016-2017/"
#get_results(url)