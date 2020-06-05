#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:59:35 2020

@author: phil

Script to scrape all of Ed's lyrics. I had to add some cunning features to 
aviod being blocked by the website.

"""

#from urllib import request

from bs4 import BeautifulSoup
from urllib import request
from time import sleep
import numpy as np



def get_soup(url):
    # pretend to be on an iphone and load some html    
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    
    req = request.Request(url) 
    req.add_header('Referer', 'https://www.google.co.uk')
    req.add_header('User-Agent', user_agent)
    resp = request.urlopen(req)
    html_doc = resp.read().decode('utf8')

    return BeautifulSoup(html_doc, 'html.parser')

    

# Load up eds lyric page whilst pretending to be a browser

#soup = BeautifulSoup(html_doc, 'html.parser')
soup = get_soup('https://www.azlyrics.com/e/edsheeran.html')

# grab all the links and shuffle them
links = [link.get('href') for link in soup.find_all('a')]


# filter for actual song links then give them a shuffle
song_links = []
for link in links:
   if '/lyrics/edsheeran/' in str(link):
       song_links.append(
          'https://www.azlyrics.com' + link.strip('..'))


np.savez('EdLinks', song_links = song_links) # save links incase we get blocked
np.random.shuffle(song_links)
                    
       
lyrics = []
titles = []
for link in song_links:
    sleep(10. * (2. + np.random.rand())) # 59th street bridge song
    soup = get_soup(link)
    page_sections = soup.find_all('div')
    titles.append(page_sections[16].get_text())
    lyrics.append(page_sections[19].get_text())
    

np.savez('EdLyrics', titles = titles, lyrics = lyrics)

#%% 
    

