# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results, sort_archive_by_date, generate_readme
from league_link_collector import sort_links
from stats import get_active_stats

#sort_archive_by_date()
#sort_links()

t = open("active_links.txt", "r") 
links = t.read()
t.close()
        
links = links.split("\n")

for link in links:
    try:
        get_results(link,"active")
        print (link)
    except:
        break

get_active_stats()

#generate_readme()