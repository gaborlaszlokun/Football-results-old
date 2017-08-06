# -*- coding: utf-8 -*-
"""
Created on Sun May 21 12:04:43 2017

@author: ASUS
"""

import urllib2
import bs4
import os
import pandas as pd

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
        half_line = "NaN,NaN,NaN"
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
        half_line = halftime[0] + "," + halftime[1] + "," + halftime_letter
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
    new_filename += ".csv"
    return new_filename

def get_results(url, where):
    index = 0
    filename = url.replace("http://www.worldfootball.net/all_matches/","").replace("/","")
    div = (filename.split("-")[0]).upper()
    div = div.replace("BUNDESLIGA","GER")
    filename = format_filename(filename)
    
    path = where + "/" + div
    filename = path + "/" + filename
    
    columns = ['Div','Date','Time','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR']
    result_df = pd.DataFrame(columns=columns)
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
                    result = format_result(result).split(",")
                    time = td[1].getText()
                    homeTeam = td[2].getText()
                    awayTeam = td[4].getText()
                    fthg = result[0]
                    ftag = result[1]
                    ftr = result[2]
                    hthg = result[3]
                    htag = result[4]
                    htr = result[5]
                    result_line_df = pd.DataFrame([[div, date, time, homeTeam, awayTeam, fthg, ftag, ftr, hthg, htag, htr]], columns=columns, index = [index])
                    index += 1
                    result_df = result_df.append(result_line_df)
            
        except:
            None
    if result_df.empty is False:
        if not os.path.exists(path):
                os.makedirs(path)
        result_df['Date'] =pd.to_datetime(result_df['Date'], dayfirst = [True])
        result_df = result_df.sort_values(['Date', 'Time'], ascending=[True, True])
        result_df.to_csv(filename, sep=',', encoding='utf-8', index=False)

def sort_archive_by_date():
    for folder in os.listdir("archive"):
        for file in os.listdir("archive/" + str(folder)):
            filename = "archive/" + str(folder) + "/" + str(file)
            if ".csv" in filename:
                results = pd.read_csv(filename)
                old_results = results
                results['Date'] =pd.to_datetime(results['Date'], dayfirst = [True])
                results = results.sort_values(['Date', 'Time'], ascending=[True, True])
                if results.equals(old_results) == False:
                    results.to_csv(filename, sep=',', encoding='utf-8', index=False)
                    print filename

#def generate_readme():
text = "# Football-results\n\n## Main attributes:\n\n- Division\n- Date\n- Time\n- Home Team\n- Away Team\n- FullTime Home Goals\n- FullTime Away Goals\n- FullTime Result\n- HalfTime Home Goals\n- HalfTime Away Goals\n- HalfTime Result\n\n"
text += "#### " + str(len(os.listdir("active"))) + " countries from the present\n\n"
countries = "|Country|Number of seasons|\n| -------------| -------------:|\n"
for folder in os.listdir("archive"):
    if "_" not in folder:
        countries += "|" + folder + "|" + str(len(os.listdir("archive/" + str(folder)))) + "|\n" 
        
text += "#### " + str(len(os.listdir("archive")) - 1) + " countries from the past (cleaned and merged):\n\n" + countries + "\n[Used source](http://www.worldfootball.net/)"

print text

t = open("README.md", "w")  
t.write(text)
t.close()
