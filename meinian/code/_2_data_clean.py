# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:07:03 2018
清洗缺失数据
@author: Administrator
"""
import pandas as pd
import numpy as np

def step_2():
    def clean_label(x):
        x=str(x)
        if '+' in x:#16.04++
            i=x.index('+')
            x=x[0:i]
        if '>' in x:#> 11.00
            i=x.index('>')
            x=x[i+1:]
        if len(x.split(sep='.'))>2:#2.2.8
            i=x.rindex('.')
            x=x[0:i]+x[i+1:]
        if '未做' in x or '未查' in x or '弃查' in x:
            x=np.nan
        if str(x).isdigit()==False and len(str(x))>4:
            x=x[0:4]
        return x
    
    def data_clean(df):
        for c in ['收缩压','舒张压','血清甘油三酯','血清高密度脂蛋白','血清低密度脂蛋白']:
            df[c]=df[c].apply(clean_label)
            df[c]=df[c].astype('float64')
        return df
    
    print('-------------删除缺失标签---------------')
    #删除空标签数据,此时是否要考虑训练集的缺失情况？
    dtr = pd.read_csv('../data/train_set.csv',encoding = 'gbk')
    
    print(dtr.shape)
    dc = data_clean(dtr)
    dc = dc[dc.收缩压.notnull()]
    dc = dc[dc.舒张压.notnull()]
    dc = dc[dc.血清甘油三酯.notnull()]
    dc = dc[dc.血清高密度脂蛋白.notnull()]
    dc = dc[dc.血清低密度脂蛋白.notnull()]
    dc = dc[dc['收缩压']>50]
    dc = dc[dc['舒张压']<400]
    dc = dc[dc['血清甘油三酯']>0]
    dc = dc[dc['血清高密度脂蛋白'] > 0]
    dc = dc[dc['血清低密度脂蛋白'] >0]
    dt = dc
    #删除缺失百分比过高的数据
    cc = []
    print('-------------删除缺失特征---------------')#不删除
    col  = list(dt.columns.values)
    col_copy = list(dt.columns.values)
    for c in col:
        d1 = dt[c]
        b = (len(dt) - d1.count())/len(dt)
        cc.append(b)
        if b >= 2:#0.99
            col_copy.remove(c)
    
    print('删除特征'+str(len(col) - len(col_copy))+'个')
    dc = dc[col_copy]
    dte = pd.read_csv('../data/test_set.csv',encoding = 'gbk')
    dte = dte[col_copy]
    print(dc.shape)
    print(dte.shape)
    print('-------------存储数据-------------------')
    import re
    col1 = list(dc.columns.values)
    for i in range(len(col1)):
        col1[i] = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", col1[i])
    col2 = list(dte.columns.values)
    for i in range(len(col2)):
        col2[i] = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", col2[i])
    dc.columns = col1
    dte.columns = col2
    dc.to_csv('../data/train_set_2.csv',encoding = 'gbk',index = False)
    dte.to_csv('../data/test_set2.csv',encoding = 'gbk',index = False)
