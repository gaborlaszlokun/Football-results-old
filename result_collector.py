# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:04:43 2017

@author: ASUS
"""

import urllib2
import bs4
from django.utils.encoding import smart_str
import os

def format_result(result):
    result_line = ""
    fulltime_letter = ""
    halftime_letter = ""
    half_line = ""
    if "|" in result:
        if "," not in result:
            result = result.split("|")
            fulltime = result[0]
            halftime = result[1]
        elif result.count(",") == 1:
            result = result.split("|")
            result = result[1].split(",")
            fulltime = result[1]
            halftime = result[0]
        elif result.count(",") == 2:
            result = result.split("|")
            result = result[1].split(",")
            fulltime = result[1]
            halftime = result[0]
    else:
        fulltime = result
        half_line = "NaN,NaN,NaN\n"
    fulltime = fulltime.split(":")
    result_line += fulltime[0] + "," + fulltime[1]
    if fulltime[0] > fulltime[1]:
        fulltime_letter = "H"
    elif fulltime[0] < fulltime[1]:
        fulltime_letter = "A"
    else:
        fulltime_letter = "D"
    if half_line == "" :
        halftime = halftime.split(":")
        if halftime[0] > halftime[1]:
            halftime_letter = "H"
        elif halftime[0] < halftime[1]:
            halftime_letter = "A"
        else:
            halftime_letter = "D"
        half_line = halftime[0] + "," + halftime[1] + "," + halftime_letter + "\n"
    result_line += "," + fulltime_letter + "," + half_line
    return result_line

def format_filename(filename):
    filename = filename.replace("bundesliga","ger")
    new_filename = filename[:3]
    filename_arr = filename[3:].split("-")
    was_num = False
    for i in range(len(filename_arr)):
        if filename_arr[i].isdigit() and len(filename_arr[i]) == 4:
            new_filename += "-" + filename_arr[i]
            was_num = True
        elif was_num is True:
            new_filename += "-" + filename_arr[i]
#        if let.isdigit():
    new_filename += ".csv"
    return new_filename

def get_results(url, where):
    
    filename = url.replace("http://www.worldfootball.net/all_matches/","").replace("/","")
    country_short = (filename.split("-")[0]).upper()
    country_short = country_short.replace("BUNDESLIGA","GER")
    filename = format_filename(filename)
    
    path = where + "/" + country_short
    filename = path + "/" + filename + ".csv"
    full_results = "Div,Date,Time,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HTHG,HTAG,HTR\n"
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()     
    soup = bs4.BeautifulSoup(data,"html.parser")
    
    table= soup.findAll('table', { "class" : "standard_tabelle" })
    
    soup = bs4.BeautifulSoup(str(table[0]),"html.parser")
    tr =  soup.findAll('tr')
    
    temptime = ""
    for i in tr:
        soup = bs4.BeautifulSoup(str(i),"html.parser")
        try:
            td = table= soup.findAll('td')
            res = str(td[5].getText())
            soup = bs4.BeautifulSoup(str(td[6]),"html.parser")
            img = soup.findAll('img')
            if "-" not in res and len(img) == 0:
                result = ""
                for char in res:
                    if char.isdigit() or char == ":" or char == ",":
                        result += char
                    elif char == "(":
                        result += "|"
                if "/" in str(td[0].getText()):
                    date = td[0].getText()
                    temptime = date
                else:
                    date = temptime
                if result != "":
                    result = format_result(result)
                    line = country_short + "," + date + "," +  td[1].getText() + "," + td[2].getText() + "," + td[4].getText() +"," + result
                    full_results += smart_str(line)
        except:
            None
        if full_results != "Div,Date,Time,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HTHG,HTAG,HTR\n":
            if not os.path.exists(path):
                os.makedirs(path)
            text = open(filename, "w")
            text.write(full_results)
            text.close()

def sort_links(links):
    active = ""
    archive = ""
    for link in links:
        usock = urllib2.urlopen(link)
        data = usock.read()
        usock.close()
        if "-:-" in data:
            active += link + "\n"
        else:
            archive += link + "\n"
        print link
    text = open("active_links.txt", "w")
    text.write(active)
    text.close()
    text = open("archive_links.txt", "w")
    text.write(archive)
    text.close()
            
