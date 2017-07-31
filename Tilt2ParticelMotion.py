# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:54:04 2017

@author: Anas Handaru
"""

import csv
import datetime
import time

# Read CSV Data
tiltFile = open('grawah.csv','rb')
reader = csv.reader(tiltFile)
data = []
for row in reader:
    data.append(row)
    
d = time.strptime(data[0][0], '%Y-%m-%d  %H:%M')
date = datetime.datetime(d.tm_year,d.tm_mon,d.tm_mday,d.tm_hour,d.tm_min)