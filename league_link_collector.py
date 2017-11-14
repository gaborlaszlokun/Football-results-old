# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:22:20 2017

@author: ASUS
"""

#import urllib2
from urllib.request import urlopen
import requests
import bs4
from result_collector import get_results, generate_readme

def get_all_links():
    base_url ="http://www.worldfootball.net"
    final_urls = ""
    
    usock = urlopen(base_url)
    data = usock.read()
    usock.close()     
    soup = bs4.BeautifulSoup(data,"html.parser")
    
    countries = soup.findAll('a', { "class" : "special" })
    for i in countries:
        url = base_url + str(i['href'])
        url = url.replace("competition","all_matches")
        url += "-2016-2017/"
        usock = urlopen(url)
        data = usock.read()
        usock.close()     
        soup = bs4.BeautifulSoup(data,"html.parser")
        seasons = soup.findAll('option')
        for j in seasons:
            if "all_matches" in j['value']:
                final_url = base_url + str(j['value']) + "\n"
                final_urls += final_url
    				
    text = open("league_links.txt", "w")
    text.write(final_urls)
    text.close()
    
def sort_links():
    get_all_links()
    t = open("archive_links.txt", "r") 
    archive_links = t.read()
    t.close()
    
    t = open("league_links.txt", "r") 
    league_links = t.read()
    t.close()
    league_links = league_links.split("\n")
    
    active_links = ""
    
    for link in league_links:
        if link not in archive_links:
#            usock = urlopen(link)
#            data = usock.read()
#            usock.close()
            data = requests.get(link).text
            if "-:-" in data:
                active_links += link + "\n"
            else:
                archive_links += "\n" + link 
                print (link)
                get_results(link,"pre_archive")
                generate_readme()
    active_links = active_links[0:-2]
    print (active_links)
    text = open("active_links.txt", "w")
    text.write(active_links)
    text.close()
    text = open("archive_links.txt", "w")
    text.write(archive_links)
    text.close()
