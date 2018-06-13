# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:50:12 2018

@author: Administrator
"""

import jieba
import re
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
from sklearn.decomposition import PCA
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def step_6():
    def k_means_code(c,ret,n_cluster,load_model,compress):
    
        dt_all = pd.read_csv('../data/tmp.csv') #using all data training the model
        vid_all = dt_all[['vid']]
        col2 = list(dt_all.columns.values)
        for i in range(len(col2)):
            col2[i] = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", col2[i])
        dt_all.columns = col2
        
        def word2vec(dt,c):
            dv = dt[c].values
            l = []
            for i in range(len(dv)):
                c =  re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！，：。？、~@#￥%……&*（）；-]+","",str(dv[i])) 
                ll = list(jieba.cut(c))
                temp = ""
                for c in ll:
                    temp = temp + c + " "
                l.append(temp)
            return l  
        raw_corpus = word2vec(dt_all,c) 
        
        #移除只出现一次的词
        texts = [[word for word in document.split()]
              for document in raw_corpus]
        from collections import defaultdict
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1
        corpus = [[token for token in text if frequency[token] > 1] for text in texts]
        for i in range(len(corpus)):
            l = ""
            ll = corpus[i]
            for j in range(len(corpus[i])):
                l = l + ll[j]+" "
            corpus[i] = l
            
        vectorizer = CountVectorizer()    
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
        weight = tfidf.toarray() 
        
        if weight.shape[1] > 500 and compress == True:
            pca = PCA(n_components = 500)
            weight = pca.fit_transform(weight)
        
        if load_model == True:
            model = joblib.load('../code/km_model/_'+str(c)+'_2.pkl')
            result = model.predict(weight)
        else:
            from sklearn.cluster import KMeans as km
            model = km(n_clusters = n_cluster,random_state = 601)
            
            model.fit(weight)
            joblib.dump(model , '../code/km_model/_'+str(c)+'_2.pkl')
            result = model.predict(weight)
            
        ret['vid'] = vid_all
        ret[c] = result
        print('==========='+str(c)+'============')
        return ret
    
    train_set = pd.read_csv('../data/train_set_2.csv',encoding = 'gbk') #取出vid
    dtr_cat = pd.read_csv('../data/dtr_cat.csv',encoding = 'gbk')
    dtr_cat = pd.concat([dtr_cat,train_set[['vid']]],axis = 1)
    
    test_set = pd.read_csv('../data/test_set2.csv',encoding = 'gbk') #取出vid
    dte_cat = pd.read_csv('../data/dte_cat.csv',encoding = 'gbk')
    dte_cat = pd.concat([dte_cat,test_set[['vid']]],axis = 1)
    
    ret = pd.DataFrame()
    #################################################
    ret = k_means_code('1001',ret,8,True,False)#窦性心律
    ret = k_means_code('1402',ret,20,True,False)#脑部血流
    ret = k_means_code('409',ret,10,True,False)#内科检查
    ret = k_means_code('426',ret,10,True,False)#心脏瓣
    ret = k_means_code('705',ret,10,True,False)#牙齿
    ret = k_means_code('912',ret,10,True,False)#甲状腺
    ret = k_means_code('1102',ret,20,True,False)#颈椎
    ret = k_means_code('3401',ret,10,True,False)
    ret = k_means_code('A301',ret,10,True,False)
    ret = k_means_code('115',ret,10,True,False)#胰腺
    ret = k_means_code('116',ret,15,True,False)#脾脏
    ret = k_means_code('126',ret,10,True,False)#胃
    ret = k_means_code('124',ret,5,True,False)#输尿管
    ret = k_means_code('A301',ret,10,True,False)#脑部
    ret = k_means_code('A202',ret,15,True,False)#胸部CT
    ret = k_means_code('A201',ret,20,True,False)#
    
    ret = k_means_code('A501',ret,10,True,False)#胃部#似乎没用
    ret = k_means_code('130',ret,10,True,False)#肾#似乎没用
    ret = k_means_code('3813',ret,10,True,False)#似乎没用
    
    ###内存不够,需要pca
    ret = k_means_code('101',ret,10,True,True)#甲状腺
    ret = k_means_code('102',ret,10,True,True)#甲状腺
    ret = k_means_code('113',ret,15,True,True)#肝
    ret = k_means_code('114',ret,15,True,True)#胆囊
    ret = k_means_code('117',ret,5,True,True)#肾
    ret = k_means_code('118',ret,5,True,True)#肾
    
    dtr_cat = pd.merge(dtr_cat,ret,on = 'vid',how = 'left')
    dte_cat = pd.merge(dte_cat,ret,on = 'vid',how = 'left')
    
    dtr_cat = dtr_cat.drop('vid',axis = 1)
    dtr_cat.to_csv('../data/dtr_cat_km.csv',encoding = 'gbk',index = False)
    dte_cat = dte_cat.drop('vid',axis = 1)
    dte_cat.to_csv('../data/dte_cat_km.csv',encoding = 'gbk',index = False)
    
    
    
    
    
