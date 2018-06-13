# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:02:11 2018
处理文本数据,分段特征
#******当前特征可能没有那么重要
@author: Administrator
"""

import pandas as pd
import numpy as np
import clean_feat_bag1 as cfb
import warnings
warnings.filterwarnings("ignore")
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False

def step_5():
    d1 = pd.read_csv('../data/dtr_txt.csv',encoding = 'gbk')
    d2 = pd.read_csv('../data/dte_txt.csv',encoding = 'gbk')
    l_tr = len(d1)
    l_te = len(d2)
    dt = pd.concat([d1,d2],axis = 0).reset_index(drop = True)
    
    col = list(dt.columns.values)
    
    new_dt = pd.DataFrame()
    
    new_dt['434'] = dt['434'].map(cfb.clean_0434)#病史
    new_dt['439'] = dt['439'].map(cfb.clean_0439)#父母遗传
    new_dt['4001'] = dt['4001'].map(cfb.clean_4001)#血管弹性
    
    new_dt['730'] = dt['730'].map(cfb.clean_730)#牙
    new_dt['947'] = dt['947'].map(cfb.clean_947)#颈椎与腰椎
    #
    ##心脏
    new_dt['420'] = dt['420'].map(cfb.clean_0420)
    new_dt['421'] = dt['421'].map(cfb.clean_0421)
    new_dt['422'] = dt['422'].map(cfb.clean_0422)
    new_dt['1002'] = dt['1002'].map(cfb.clean_1002)
    ##肺
    new_dt['425'] = dt['425'].map(cfb.clean_0425).convert_objects(convert_numeric=True)
    #肝
    new_dt['406'] = dt['406'].map(cfb.clean_406)
    new_dt['A705'] = dt['A705'].map(cfb.clean_A705)
    ##肾
    new_dt['431'] = dt['431'].map(cfb.clean_0431)
    new_dt['440'] = dt['440'].map(cfb.clean_0440).convert_objects(convert_numeric=True)
    #腹部
    new_dt['430'] = dt['430'].map(cfb.clean_430)#*
    new_dt['435'] = dt['435'].map(cfb.clean_0435)
    #淋巴结
    new_dt['911'] = dt['911'].map(cfb.clean_0911)
    
    #未知检查指标
    
    new_dt['269041'] = dt['269041'].map(cfb.clean_269041)
    new_dt['2228'] = dt['2228'].apply(cfb.clean_2228)
    new_dt['2229'] = dt['2229'].apply(cfb.clean_2228)
    new_dt['3189'] = dt['3189'].apply(cfb.clean_3189)
    new_dt['3190'] = dt['3190'].apply(cfb.clean_3189)
    new_dt['3192'] = dt['3192'].apply(cfb.clean_3189)
    new_dt['3194'] = dt['3194'].apply(cfb.clean_3189)
    new_dt['3195'] = dt['3195'].apply(cfb.clean_3189)
    new_dt['3197'] = dt['3197'].apply(cfb.clean_3197)
    new_dt['3601'] = dt['3601'].apply(cfb.clean_3601)
    new_dt['3301'] = dt['3301'].apply(cfb.clean_3301)#?
    new_dt['3303'] = dt['3303'].apply(cfb.clean_3303)#?
    new_dt['3426'] = dt['3426'].apply(cfb.clean_3426)#?
    new_dt['3485'] = dt['3485'].apply(cfb.clean_3485)#?
    new_dt['3868'] = dt['3868'].apply(cfb.clean_3868)#?
    new_dt['459271'] = dt['459271'].apply(cfb.clean_459271)#?
    new_dt['A302'] = dt['A302'].apply(cfb.clean_A302)#?
    
    #new_dt['529002'] = dt['529002'].apply(cfb.clean_529001)#??
    #new_dt['669016'] = dt['669016'].apply(cfb.clean_669016)#??
    #new_dt['669017'] = dt['669017'].apply(cfb.clean_3191)#??
    #new_dt['709039'] = dt['709039'].apply(cfb.clean_709039)#??
    #new_dt['799003'] = dt['799003'].apply(cfb.clean_799003)#??
    #new_dt['A49010'] = dt['A49010'].apply(cfb.clean_A49010)#??
    #new_dt['A49011'] = dt['A49011'].apply(cfb.clean_A49011)#??
    
    new_dt['E19002'] = dt['E19002'].apply(cfb.clean_E19002)
    new_dt['E39002'] = dt['E39002'].apply(cfb.clean_E39002)
    new_dt['E39003'] = dt['E39003'].apply(cfb.clean_E39002)
    new_dt['E49029'] = dt['E49029'].apply(cfb.clean_E49029)
    new_dt['K89001'] = dt['K89001'].apply(cfb.clean_K89001)
    new_dt['K89003'] = dt['K89003'].apply(cfb.clean_K89003)
    
    #眼睛(只看是眼底否有动脉硬化以及高血压的影响)
    new_dt['1316'] = dt['1316'].map(cfb.clean_1316)
    new_dt['1330'] = dt['1330'].map(cfb.clean_1330)
    new_dt['1331'] = dt['1331'].map(cfb.clean_1331)
    ##脑部
    new_dt['2302'] = dt['2302'].map(cfb.clean_2302)
    
    #男性标注为 1 ； 女性标注为 2
    def jdg(l):
        for i in range(len(l)):
            if l[i] != 0:
                l[i] = 1
            else:
                l[i] =  0
        return l
                
    def bol_man(x):
        if x == -999:
            return 0
        else:
            return 1
    dt.fillna(-999,inplace = True)
    
    vot1_man = dt['120'].map(bol_man).values
    vot2_man = dt['981'].map(bol_man).values
    vot3_man = dt['983'].map(bol_man).values
    vot4_man = dt['984'].map(bol_man).values
    is_man = np.array([[vot1_man],[vot2_man],[vot3_man],[vot4_man]])
    is_man2 = is_man[0,:] + is_man[1,:] + is_man[2,:] + is_man[3,:]
        
    def bol_woman(x):
        if x == -999:
            return 0
        else:
            return 1
    dt.fillna(-999,inplace = True)
    
    vot1_woman = dt['121'].map(bol_woman).values
    vot2_woman = dt['122'].map(bol_woman).values
    vot3_woman = dt['123'].map(bol_woman).values
    vot4_woman = dt['509'].map(bol_woman).values
    vot5_woman = dt['537'].map(bol_woman).values
    is_woman = np.array([[vot1_woman],[vot2_woman],[vot3_woman],[vot4_woman],[vot5_woman]])
    is_woman2 = is_woman[0,:] + is_woman[1,:] + is_woman[2,:] + is_woman[3,:] + is_woman[4,:]
    
    is_man = is_man2[0]
    is_woman = is_woman2[0]
    is_man = jdg(is_man)
    is_woman = jdg(is_woman)
    gender = []
    for i in range(len(is_man)):
        if is_man[i]!=0 and is_woman[i] == 0:
            gender.append(1)   #男性
        elif is_man[i]==0 and is_woman[i] != 0:
            gender.append(2)   #女性
        else:
            gender.append(0)   #未知
    new_dt['gender'] = gender
    
    #
    def splitDt(dt,train_row,test_row):
        d1 = dt.iloc[0:train_row]
        d2 = dt.iloc[train_row:]
        d1 = d1.reset_index(drop = True)
        d2 = d2.reset_index(drop = True)
        return d1,d2 
    dtr_cat,dte_cat = splitDt(new_dt,l_tr,l_te)
    
    dtr_cat.to_csv('../data/dtr_cat.csv',encoding = 'gbk',index = False)
    dte_cat.to_csv('../data/dte_cat.csv',encoding = 'gbk',index = False)
    
    #a = new_dt['431'].dropna().values
    #print(np.unique(a))
    #print(np)
    #import matplotlib.pyplot as plt
    #plt.figure()
    #plt.hist(a,bins = 20)
    #plt.show()
