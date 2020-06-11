# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:22:29 2020

@author: Olivia
"""


from googletrans import Translator


def main():
    translator = Translator()
    result = translator.translate('Jak się masz?')
    print(result.text)
    
main()