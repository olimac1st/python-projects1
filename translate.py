# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:22:29 2020

@author: Olivia
"""


from googletrans import Translator
import requests
import json

def googletrans():
    translator = Translator()
    result = translator.translate('Jak się masz?', dest='pl')
    print(result.text)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate.pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data=data)
    json_data = json.loads(response.text)
    print(type(response.text))
    print(json_data['contents']['translated'])
    
piratetrans('i like eating apples')