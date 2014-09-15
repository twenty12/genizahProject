
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 22:46:11 2014

@author: danielgladstone
"""


import urllib2
import lxml
import requests
import re
#import mechanize
from bs4 import BeautifulSoup
import csv
import lxml.html
from urlparse import urlparse

print('------------------------------')



changingurl = "http://genizah.bodleian.ox.ac.uk/search/results?start=10"

url = urllib2.urlopen(changingurl).read()

soup = BeautifulSoup(url)

table = open('/Users/danielgladstone/Desktop/table.csv','w')

f = csv.writer(table)
f.writerow(["Name","Link"])

href=re.compile("profile")

links = soup.find_all('a',href = re.compile("profile"))

for link in links:
    if link:
        links.remove(link)
    name = link.contents
    FullLink = link.get('href')
    f.writerow([name,FullLink])
