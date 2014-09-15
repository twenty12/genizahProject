# -*- coding: utf-8 -*-
"""
Created on Sat May 24 21:04:32 2014

@author: daniel
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 23 22:46:11 2014

@author: danielgladstone
"""

import os.path
import urllib2
import csv
import time
from bs4 import BeautifulSoup

destination = '/Users/danielgladstone/Google Drive/Genizah/Lists/complete.csv'

URL_List = '/Users/danielgladstone/Google Drive/Genizah/Lists/Tittle-URL.csv'

if os.path.isfile(destination) == True:    #prevents appending old version
    os.remove(destination)
    
table = open(destination,'w')

f = csv.writer(table)
f.writerow(['Title','Name', 'Part of volume', 'Physical description', 'Acquisition', 'destination', 'Languages', 'Authors', 'Mentions', 'Party to the Deed', 'Key Words', 'Notes', 'URL'])

#3751
for i in range(3751):
    line_number = i+3
    with open(URL_List, 'rb') as F:
        mycsv = csv.reader(F)
        mycsv = list(mycsv)
        TI = mycsv[line_number][0]
        UL = mycsv[line_number][1]
        
    URL = 'http://genizah.bodleian.ox.ac.uk' + UL
        
    #URL = 'http://genizah.bodleian.ox.ac.uk/profile/manuscript/561fe9a9-8b7f-4fb5-a753-7989cd861627#a8b53611-0710-4b15-9ab7-b08ae63f0a03'

    print ' '
    print '++++ I have done',i,'of the page scrapes. NEXT PLEASE ++++'
    print ' '

    url = urllib2.urlopen(URL).read()
    
    soup = BeautifulSoup(url)
    
    table = open(destination,'a')
    
    alll = soup.find_all('h4') #<class 'bs4.element.Tag'>
    
    key = soup.find_all('p') #<class 'bs4.element.Tag'>    

    name = soup.find_all('h3')

    PV = []; FD = []; AQ = []; LO = []; LN = []; AU = []; ME = []; PD = []; KW = []; NM = []; NO = []
    
    for n in name:
        nn = n.find_all('span')
        for nnn in nn:
            NM.append(unicode(nnn.string))

    for no in key:
        if no.string == 'Notes:':
            for nono in no:
                for nono in no.parent.find_all('li'):
                    NO.append(nono.get_text()) #already Unicode becuase of get_text()
                    
    for k in key:
        if k.string == 'Keywords:':
            for kk in k.parent.find_all('li'):
                KW.append(unicode(kk.string))
    for heading in alll:
                

        outside = heading.parent
        for test in outside:
            
            if outside.h4.string == 'Part of volume:':
                PV.append(unicode(outside.p.string))
                break
                
            if outside.h4.string == 'Physical Description:':
                for fd in outside.find_all('p'):
                    FD.append(fd.get_text()) #already Unicode
                break
                
            if outside.h4.string == 'Acquisition:':     
                for ad in outside.find_all('p'):
                    AQ.append(ad.get_text())
                break
            
            if outside.h4.string == 'Location:':
                for ld in outside.find_all('a'):
                    LO.append(ld.get_text())
                break
            
            if outside.h4.string == 'Languages:':
                for la in outside.find_all('p'):
                    LN.append(la.get_text())
                break
  
    for auth in outside.find_all('h4'):
        if auth.get_text()=='Authors:':
            for auths in outside.a:
                AU.append(auths.get_text().encode('ascii','ignore'))

        if auth.get_text()=='Mentions:':
            for mens in outside.find_all('a'):
                ME.append(mens.get_text())

        if auth.get_text()=='Party to the deed:':
            for mens in outside.find_all('a'):
                PD.append(mens.get_text())
            break
        
    time.sleep(2)         
    
    f = csv.writer(table)
    data_from_page = [TI, NM, PV, FD, AQ, LO, LN, AU, ME, PD, KW, NO, URL]    
    print data_from_page
    f.writerow(data_from_page)