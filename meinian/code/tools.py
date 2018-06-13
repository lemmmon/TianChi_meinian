# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:40:49 2018

@author: Administrator
"""
import pandas as pd
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def getCross(dt,col):
    for i in range(len(col)):
        for j in range(len(col)):
            if i != j:
                c1 = col[i]
                c2 = col[j]
                dt[str(c1)+'+'+str(c2)] = dt[c1].add(dt[c2])
                dt[str(c1)+'-'+str(c2)] = dt[c1].sub(dt[c2])
                dt[str(c1)+'*'+str(c2)] = dt[c1].mul(dt[c2])
                dt[str(c1)+'/'+str(c2)] = dt[c1].div(dt[c2])    
    return dt



