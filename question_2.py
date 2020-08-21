# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:35:06 2020

@author: Helene Stabell
"""



def to_camel_case(text):
    words = text.split()
    sep_camels = []
    str1 = "" 
    
    for word in words:
        capt = word.capitalize()
        sep_camels.append(capt)
    
    return (str1.join(sep_camels)) 
    



 
    
    
    
       
    
        
