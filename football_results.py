# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results, sort_archive_by_date, generate_readme
from league_link_collector import sort_links
from stats import get_active_stats

import datetime
import time
from time import gmtime, strftime

#while True:
#    try:
#        now = datetime.datetime.now()
#        if now.hour == 0 and now.minute < 30:

#sort_archive_by_date()
#sort_links()

t = open("active_links.txt", "r") 
links = t.read()
t.close()
        
links = links.split("\n")
            #
for link in links:
    try:
        get_results(link,"active")
        print link
    except:
        print "Ajjajj..."

get_active_stats()

#generate_readme()

#        print "Checked at:", strftime("%H:%M:%S", gmtime())  
#        time.sleep(600)
        
#    except:
#        print "Something went wrong... Try reconnecting..."
#        time.sleep(600)