# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:10:41 2020

@author: Helene Stabell
"""


customer = ['James','John','Robert','Mary','Patricia','Jennifer']
salary  = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]



def fraud_detection():
    
    customers_to_investigate = []
    
    for i in range(len(customer)):
       
        name = customer[i]
        earns = int(salary[i])
        tax = int(taxes[i])
        tax_rate = tax / earns
    
        if earns < 555000:
            pass
        else:
            if tax_rate < 0.30:
                customers_to_investigate.append(name)
       
    print(f'Your bank should investigate {customers_to_investigate} for fraud.')
    