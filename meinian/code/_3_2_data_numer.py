# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 10:35:30 2018
处理连续特征
@author: Administrator
"""
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False

def step_4():
    d1 = pd.read_csv('../data/dtr_numer.csv',encoding = 'gbk',low_memory=False)
    aim1 = d1['收缩压'].values#正态
    aim2 = d1['舒张压'].values#正态
    aim3 = d1['血清甘油三酯'].values#右偏
    aim4 = d1['血清高密度脂蛋白'].values#右偏
    aim5 = d1['血清低密度脂蛋白'].values#右偏
    d1 = d1.drop('收缩压',axis = 1)
    d1 = d1.drop('舒张压',axis = 1)
    d1 = d1.drop('血清甘油三酯',axis = 1)
    d1 = d1.drop('血清高密度脂蛋白',axis = 1)
    d1 = d1.drop('血清低密度脂蛋白',axis = 1)
    #    col = list(d1.columns.values)
    d2 = pd.read_csv('../data/dte_numer.csv',encoding = 'gbk',low_memory=False)
    l_tr = len(d1)
    l_te = len(d2)
    
    dt = pd.concat([d1,d2],axis = 0).reset_index(drop = True)
    
    import clean_feat_bag1 as cfb
    dt['424'] = dt['424'].apply(cfb.clean_feat_0424)#心跳
    dt['424'] = dt['424'].convert_objects(convert_numeric=True)
    dt = dt.convert_objects(convert_numeric=True)
    dt['BMI'] = dt['2403'].div(dt['2404'].mul(dt['2404']))  
    
    #替换中文字符
    dt = dt.replace('未见',np.nan)
    
    #数据保存
    def splitDt(dt,train_row,test_row):
        d1 = dt.iloc[0:train_row]
        d2 = dt.iloc[train_row:]
        d1 = d1.reset_index(drop = True)
        d2 = d2.reset_index(drop = True)
        return d1,d2 
    dtr,dte = splitDt(dt,l_tr,l_te)
    
    dtr.to_csv('../data/dtr_numer2.csv',index = False,encoding = 'gbk')
    dte.to_csv('../data/dte_numer2.csv',index = False,encoding = 'gbk')

    
