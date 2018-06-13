# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:50:52 2018
获得五个指标的基本预测值
@author: Administrator
"""

import lightgbm as lgb
import pandas as pd
import numpy as np

def step_7():
    aim = pd.read_csv('../data/dtr_numer.csv',encoding = 'gbk',low_memory=False)
    
    a1 = aim['收缩压'].values
    a2 = aim['舒张压'].values
    a3 = aim['血清甘油三酯'].values
    a4 = aim['血清高密度脂蛋白'].values
    a5 = aim['血清低密度脂蛋白'].values
    
    sub = pd.read_csv('../data/meinian_round1_test_b_20180505.csv',encoding='gbk')
    for i in range(5):
        if i == 0:
            label = a1
            dtr_numer = pd.read_csv('../data/dtr_numer2.csv',encoding = 'gbk')
            dte_numer = pd.read_csv('../data/dte_numer2.csv',encoding = 'gbk')
            dtr_cat = pd.read_csv('../data/dtr_cat_km.csv',encoding = 'gbk')
            dte_cat = pd.read_csv('../data/dte_cat_km.csv',encoding = 'gbk') 
            
            dtr = pd.concat([dtr_numer,dtr_cat],axis = 1)
            dte = pd.concat([dte_numer,dte_cat],axis = 1)
        if i == 1:
            label = a2
            dtr_numer = pd.read_csv('../data/dtr_numer2.csv',encoding = 'gbk')
            dte_numer = pd.read_csv('../data/dte_numer2.csv',encoding = 'gbk')
            dtr_cat = pd.read_csv('../data/dtr_cat_km.csv',encoding = 'gbk')
            dte_cat = pd.read_csv('../data/dte_cat_km.csv',encoding = 'gbk') 
            
            dtr = pd.concat([dtr_numer,dtr_cat],axis = 1)
            dte = pd.concat([dte_numer,dte_cat],axis = 1)
        if i == 2:
            label = a3
            dtr_numer = pd.read_csv('../data/dtr_numer2.csv',encoding = 'gbk')
            dte_numer = pd.read_csv('../data/dte_numer2.csv',encoding = 'gbk')
            dtr_cat = pd.read_csv('../data/dtr_cat_km.csv',encoding = 'gbk')
            dte_cat = pd.read_csv('../data/dte_cat_km.csv',encoding = 'gbk') 
            
            dtr = pd.concat([dtr_numer,dtr_cat],axis = 1)
            dte = pd.concat([dte_numer,dte_cat],axis = 1)
        if i == 3:
            label = a4
            dtr_numer = pd.read_csv('../data/dtr_numer2.csv',encoding = 'gbk')
            dte_numer = pd.read_csv('../data/dte_numer2.csv',encoding = 'gbk')
            dtr_cat = pd.read_csv('../data/dtr_cat_km.csv',encoding = 'gbk')
            dte_cat = pd.read_csv('../data/dte_cat_km.csv',encoding = 'gbk') 
            
            dtr = pd.concat([dtr_numer,dtr_cat],axis = 1)
            dte = pd.concat([dte_numer,dte_cat],axis = 1)
        if i == 4:
            label = a5
            dtr_numer = pd.read_csv('../data/dtr_numer2.csv',encoding = 'gbk')
            dte_numer = pd.read_csv('../data/dte_numer2.csv',encoding = 'gbk')  
            dtr_cat = pd.read_csv('../data/dtr_cat_km.csv',encoding = 'gbk')
            dte_cat = pd.read_csv('../data/dte_cat_km.csv',encoding = 'gbk') 
            
            dtr = pd.concat([dtr_numer,dtr_cat],axis = 1)
            dte = pd.concat([dte_numer,dte_cat],axis = 1)
        
        
        print(i)
        model = lgb.LGBMRegressor(
                    n_estimators = 2500,
                    learning_rate = 0.01,
                    random_state = 601)
        model.fit(dtr.values,np.log(label))
        ans = model.predict(dte.values)  
        
        if i == 0:
            sub['收缩压'] = np.round(np.exp(ans),3)
        if i == 1:
            sub['舒张压'] = np.round(np.exp(ans),3)
        if i == 2:
            sub['血清甘油三酯'] = np.round(np.exp(ans),3)
        if i == 3:
            sub['血清高密度脂蛋白'] = np.round(np.exp(ans),3)
        if i == 4:
            sub['血清低密度脂蛋白'] = np.round(np.exp(ans),3)
#    import time
#    sub.to_csv('../submit/submit'+time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))+'.csv',encoding = 'gbk',index = False,header = None)
    sub.to_csv('../submit/submit1.csv',encoding = 'gbk',index = False,header = None)
    
        
