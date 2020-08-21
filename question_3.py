# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:06:55 2020

@author: Helene Stabell
"""
Jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}


call_points = 10 
meeting_points = 30 
sale_points = 100
# bonus points for +150 calls, +20meetings, +5sales 

def employee_score(name):
    
    e_call_score = name['calls'] * call_points
    e_meeting_score = name['meetings'] * meeting_points
    e_sale_score = name['sales'] * sale_points
    
    total_score = e_call_score + e_meeting_score + e_sale_score
    
    if name['calls'] > 150:
        total_score += 100
    
    if name['meetings'] > 20:
        total_score += 100
        
    if name['sales'] > 5:
        total_score += 100
        
    name['score'] = total_score
    
    print(name)
        
    print(f'The total score of the employee is {total_score} points. Well done!')
    

    