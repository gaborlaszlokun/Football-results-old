# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:37:39 2017

@author: ASUS
"""

from result_collector import get_results
from league_link_collector import sort_links


import datetime
import time
from time import gmtime, strftime

#while True:
#    try:
#        now = datetime.datetime.now()
#        if now.hour == 0 and now.minute < 30:

sort_links()
#            print "Links checked at:", strftime("%H:%M:%S", gmtime())  
    
t = open("active_links.txt", "r") 
links = t.read()
t.close()
        
links = links.split("\n")
            #
for link in links:
    get_results(link,"active")
    print link
#        print "Checked at:", strftime("%H:%M:%S", gmtime())  
#        time.sleep(600)
        
#    except:
#        print "Something went wrong... Try reconnecting..."
#        time.sleep(600)
      
    
    
#link = "http://www.worldfootball.net/all_matches/irq-super-league-2016-2017/"
#get_results(link,"active")
   
#check_file(links) 

#url = "http://www.worldfootball.net/all_matches/alb-kategoria-superiore-2016-2017/"
#get_results(url)