# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:22:20 2017

@author: ASUS
"""

import urllib2
import bs4
from django.utils.encoding import smart_str

base_url ="http://www.worldfootball.net"

usock = urllib2.urlopen(base_url)
data = usock.read()
usock.close()     
soup = bs4.BeautifulSoup(data,"html.parser")

countries = soup.findAll('a', { "class" : "special" })
for i in countries:
    url = base_url + str(i['href'])
    url = url.replace("competition","all_matches")
    url += "-2016-2017/"
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()     
    soup = bs4.BeautifulSoup(data,"html.parser")
    seasons = soup.findAll('option')
    for j in seasons:
        if "all_matches" in j['value']:
            final_url = base_url + str(j['value']) + "\n"
            print final_url
            text = open("league_links.txt", "a")
            text.write(final_url)
            text.close()
