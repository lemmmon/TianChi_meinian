# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:07:03 2018
分割训练集与测试集中的文本特征与数值特征
@author: Administrator
"""

import pandas as pd
import numpy as np
import jieba
import re

def step_3():
    dt = pd.read_csv('../data/train_set_2.csv',encoding = 'gbk')
    d2 = pd.read_csv('../data/test_set2.csv',encoding = 'gbk')
    print(dt.shape)
    col_numer = []
    col_txt = []
    col1 = list(dt.columns.values)
    col2 = list(d2.columns.values)
    
    d2.columns = col2
    d2 = d2[list(dt.columns.values)]
    
    
    pr = pd.read_csv('../code/data_type.csv',encoding = 'gbk')#加上文本，得分0.03029
    col_numer = list(pr[pr['type'] == 'float64'].name.values)
    col_txt = list(pr[pr['type'] == 'object'].name.values)
    print('---------分割数据-----------')
    #fix有些分错了
    col_rem = ['421','425','440','435','100010','2228','2229','2230','2231','2233'
               ,'3189','3194','3195','3430','A201','439026','V69001','V69002',
               '4314','319276','369104','G99031','G99032','G99033','G99034','G99035',
               'G99036','G99037','G99038','G99040','G99041','G99042','G99043','G99044',
               'G99045','G99046','G99047','G99048','G99049','G99050','G99051','G99052',
               'F39012','K59033','229070','G99137','G99138','G99139','G99140','G99141',
               'G99142','G99143','G99144','G99145','G99146','G99147','G99148','G99149',
               'G99150','E49034','E19075','E19076','E19077','E19078','709051','579039',
               '579040','579041','579042','579043','300103','179220',
               '702','703','715','974','300018','300019','3203','3730','3738','3207',
               '3400','3429','I49012','3196','436','300005','300062',
               #空列(训练集中一个值都没有)
               '69078', '69079', '69080', '69081', '69082', '69083', '69084', '69085', 
               '69086', '69089', '69090', '69091', '69092', '1847', '199112', '21A009', 
               '21A274', '2330', '2433', '269059', '269060', '369034', '369035', '369059',
               '3815', '419007', '449131', '4502', '709029', '839001', '839002', '839003',
               '839004', '839005', '839007', '839008', '839009', '839010', '8401', '909036', 
               'I49004', 'I49010', 'I49016', 'J29102', 'J29103', 'L29001', 'L69005', 'Y29003',
               'Y29004'
                        ]
    for c in col_rem:
        if c in col_numer:
            print(c)
            col_numer.remove(c)
            col_txt.append(c)
        
    delt = ['439026','V69001','V69002','4314','369104','F39012','K59033','229070','G99137',
            'G99138','G99139','G99140','G99141','G99142','G99143','G99144','G99145','G99146',
            'G99147','G99148','G99149','G99150','E49034','E19075','E19076','E19077','E19078',
            '709051','579039','579040','579041','579042','579043','179220','69092','1847','199112',
            '2433','369034','369059','419007','709029','839001','839002','839003','839004','839005',
            '839007','839008','839009','839010','909036','I49010','J29102','J29103','L29001','L69005',
            'Y29003','Y29004']
    
    for c in delt:
        if c in col_numer:
            col_numer.remove(c)
        if c in col_txt:
            col_txt.remove(c)
        
    #训练集为dt 测试集为d2
    d1_numer = dt[col_numer]
    d1_txt = dt[col_txt]
    d2_numer = d2[col_numer]
    d2_numer = d2_numer.drop('收缩压',axis = 1)
    d2_numer = d2_numer.drop('舒张压',axis = 1)
    d2_numer = d2_numer.drop('血清甘油三酯',axis = 1)
    d2_numer = d2_numer.drop('血清高密度脂蛋白',axis = 1)
    d2_numer = d2_numer.drop('血清低密度脂蛋白',axis = 1)
    d2_txt = d2[col_txt]
    
    d1_numer.to_csv('../data/dtr_numer.csv',index = False, encoding = 'gbk')
    d1_txt.to_csv('../data/dtr_txt.csv',index = False, encoding = 'gbk')
    d2_numer.to_csv('../data/dte_numer.csv',index = False, encoding = 'gbk')
    d2_txt.to_csv('../data/dte_txt.csv',index = False, encoding = 'gbk')
               
        
        
        
        
                 
        
        
        
