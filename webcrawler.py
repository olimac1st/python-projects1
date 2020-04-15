# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:08:10 2020

@author: Olivia
"""


import urllib.request
from bs4 import BeautifulSoup

print('Getting staff urls...')

staff_url = 'http://wa.amu.edu.pl/wa/en/staff_list'
response = urllib.request.urlopen(staff_url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

print(doc)
