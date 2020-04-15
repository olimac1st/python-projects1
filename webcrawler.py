# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:08:10 2020

@author: Olivia
"""


import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

print('Getting staff urls...')

staff_url = 'http://wa.amu.edu.pl/wa/en/staff_list'
response = urllib.request.urlopen(staff_url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

staff_content = doc.find(id='tresc_wlasciwa')

links = staff_content.find_all('a')

urls = []

for link in links:
    if len(link.get_text()) > 1:
        base_url= 'http://wa.amu.edu.pl'
        url =  urllib.parse.urljoin(base_url, link['href'])
        urls.append(url)
    
print('Urls found:')
print('\n'.join(urls))
