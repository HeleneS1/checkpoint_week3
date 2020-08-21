# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:32:03 2020

@author: Helene Stabell
"""
def to_snake_case(text):
    capitals = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sep_snake = []
    str1 = ""
    
    for character in text:
        if character in capitals:
            c = '_' + (str(character)).lower()
            sep_snake.append(c)    
        elif character.isnumeric():
            sep_snake.append('_'+character+'_')
        elif character == ' ':
            print('Wrong format dude! Try again.')
        else:
            sep_snake.append(character)
            
    output_line = str(str1.join(sep_snake))
    output_line.replace('__','_')
    return (output_line[1:-1])

to_snake_case('This65Has7')





#%%

def to_camel_case(text):
    words = text.split()
    sep_camels = []
    str1 = "" 
    
    for word in words:
        capt = word.capitalize()
        sep_camels.append(capt)
    
    return (str1.join(sep_camels)) 
    
