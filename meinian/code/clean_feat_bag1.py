# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:34:02 2018

@author: Administrator
"""
import tools as tols
import re
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def clean_feat_0424(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if tols.is_number(x):
        return x
    else:
        if '过缓' in x:
            return  50
        elif '过速' in x:
            return 110
        elif '正常' in x:
            xx = re.sub("\D", "", x) 
            return xx if len(xx) != 0 else 75

def clean_0101(x):#甲状腺
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未见' in x and '异常' in x or '正常'in x:
        return 1 
    elif '紊乱' in x or '欠均匀' in x or '不均匀' in x or '见一个低回声结节' in x:
        return 2
    else:
        return 0

def clean_0420(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未' in x or '正常' in x: 
        return 0
    elif '心音弱' in x: 
        return 1
    elif '强弱不等' in x: 
        return 2
    elif '心音遥远' in x:
        return 3
    elif '心音强' in x or '有力' in x:
        return 4
    return 5

def clean_0421(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '整齐' in x or x == '齐': 
        return 0
    elif '心律不齐' in x: 
        return 1
    elif '偶发早搏' in x: 
        return 2
    elif '窦性心律不齐' in x:
        return 3
    elif '频发早搏' in x:
        return 4
    elif '早搏' in x:
        return 5
    elif '心律绝对不齐' in x:
        return 6
    else:
        return 7

def clean_0422(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未见异常' in x: 
        return 0
    elif '无神经定位体征' in x: 
        return 1
    elif '病理反射未引出' in x: 
        return 2
    elif '生理反射存在' in x:
        return 3
    elif '无神经定位体征' in x:
        return 4

def clean_0434(x):#病史
    x = str(x)
    if x == "nan":
        return np.NaN
    if '无' in x or '健康' in x:
        return 0
    elif '高' in x and '血压' in x and '糖尿病' in x:
        return 1
    elif '高' in x and '血压' in x and '脂肪肝' in x:
        return 2
    elif '高' in x and '血压' in x and '冠心病' in x:
        return 3
    elif '高血压史（治疗中）' in x:
        return 4
    elif '高血压史（未治疗）' in x:
        return 5
    elif '高血压史（间断治疗）' in x:
        return 6
    elif '高血压史（中断治疗）' in x:
        return 7
    elif '剖宫产术后' in x:
        return 8
    elif '脂肪肝史' in x:
        return 9
    elif '糖尿病史（治疗中）' in x:
        return 10
    elif '血压偏高' in x:
        return 11
    elif '心脏' in x:
        return 12
    elif '胃' in x:
        return 13
    elif '血脂偏高' in x:
        return 14
    elif '尿酸偏高' in x or '痛风' in x:
        return 15
    elif '甲状腺' in x:
        return 16
    elif '高血压' in x:
        return 17
    elif '肝' in x:
        return 18
    return 19
    
def clean_4001(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '良好' in x or '正常' in x: 
        return 0
    if '未见狭窄' in x:  
        return 0
    elif '轻度减弱' in x: 
        return 1
    elif '减弱趋势' in x: 
        return 2
    elif '中度减弱' in x:
        return 3
    elif '重度减弱' in x:
        return 4
    elif '轻度硬化' in x: 
        return 5
    elif '硬化' in x:
        return 6
    elif '可能' in x:
        return 7
    else:
        return 8

def clean_0425(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '正常' in x or '未见异常' in x: 
        return 0
    elif '粗糙' in x:
        return 1
    else:
        return x

def clean_0431(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '无' in x or '未见异常' in x: 
        return 0
    elif '痛' in x:
        return 1

def clean_0435(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未见' in x and '异常' in x: 
        return 0
    if '正常' in x: 
        return 1
    if '软' in x:
        return 2  
    if '不满意' in x:
        return 3
    if '有压痛' in x:
        return 4
def clean_0440(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '无叩痛' in x or '未见异常' in x or '无重大手术史' in x:
        return 0
    if '左肾有叩痛' in x:
        return 1
    if '双肾有叩痛' in x:
        return 2
    if '右肾有叩痛' in x:
        return 3
  
def clean_0911(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '不肿大' in x or '未见明显异常' in x or '未触及' in x or '无压痛' in x:
        return 0
    elif '肿大' in x:
        return 1
    else:
        return 2

def clean_1002(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '正常' in x or '未见' in x or 'HR' in x:
        return 0
    if '过缓' in x:
        return 1
    return 2

def clean_1316(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '硬化' in x and ('Ⅰ' in x or '1' in x or '一' in x):
        return 1
    elif '硬化' in x and ('Ⅱ' in x or '2' in x or '二' in x):
        return 2
    elif '高血压' in x:
        return 3
    else:
        return 0
    
def clean_1330(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '硬化' in x:
        return 1
    else:
        return 0 
    
def clean_1402(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未见明显异常' in x or '正常' in x or '未见异常'in x:
        return 0
    if '弹性' in x and '降低' in x:
        return 1
    if '慢' in x:
        return 2
    if '快' in x:
        return 3
    if '硬化' in x:
        return 4
    return 5
    
def clean_2228(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+-' in x:
        return 2
    elif '阴性' in x or '-' in x:
        return 0;
    elif '阳性' in x or '+' in x:
        return 1
    
def clean_2302(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if x == '亚健康':
        return 0
    elif '健康' in x:
        return 1 
    if '疾病' in x:
        return 2
    return 3

def clean_30007(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if 'Ⅰ' in x or 'Ⅰ°' in x:
        return 1
    if 'Ⅱ' in x or 'II' in x or 'ii°' in x:
        return 2
    if 'Ⅲ' in x or 'III' in x or 'iii°' in x:
        return 3
    if 'Ⅳ' in x:
        return 4
    if '中度' in x:
        return 5
    if '未见异常' in x or '正常' in x:
        return 6
    return 7

def clean_3189(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+++' in x:
        return 4
    if '++' in x:
        return 5
    if '阴性' in x or '-' in x:
        return 0;
    if '阳性' in x or '+' in x:
        return 1
    if '0' in x:
        return 2
    return 3


def clean_3430(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '阴性' in x:
        return 2
    if '阳性' in x:
        return 3 
    if '+-' in x:
        return 4 
    if '++' in x:
        return 5 
    if '+++' in x:
        return 6 
    if '0(-)' in x:
        return 7 
    if '-' in x:
        return 1 
#    return 8

def clean_3197(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+-' in x:
        return 1 
    if '-' in x:
        return 2
    if '阴性' in x:
        return 3
    if '+' in x:
        return 4 
    
def clean_406(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未' in x:
        return 2
    if '肝肿大' or '可触及' in x:
        return 1
    return 3
    
def clean_430(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '软' in x:
        return 1
    elif '中' in x:
        return 2
    elif '硬' in x:
        return 3
    return 4
    
def clean_0439(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '无' in x or '未' in x:
        return 1
    elif '高血压' in x and '糖尿病' in x:
        return 2
    elif '高血压' in x:
        return 3
    elif '糖尿病' in x:
        return 4
    return 5

def clean_730(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '有' in x or '义齿' in x or '瓷' in x:
        return 1
    return 2

def clean_947(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '活动自如' in x or '未见异常' in x or '活动正常' in x:
        return 1
    elif '生理弯曲' == x:
        return 2
    elif '颈' in x and '腰' in x:
        return 3
    elif '颈' in x:
        return 4
    elif '腰' in x:
        return 5
    elif '脊柱' in x:
        return 6
    return 7
        
def clean_1331(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '高' in x:
        return 1
    return 0
    
def clean_21A014(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未见' in x:
        return 1
    elif '炎性反应性细胞改变' in x:
        return 2
    elif '建议' in x:
        return 3
    else:
        return 4

def clean_269041(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '阴性' in x or '-' in x:
        return 1
    elif '阳性' in x:
        return 2
    
def clean_269044(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '少许' in x:
        return 1
    return 0
    
def clean_2901(x):  #都是见报告单
    x = str(x)
    if x == "nan":
        return np.NaN
    if '见' in x:
        return 1
    return 0  
    
def clean_3301(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '阴' in x:
        return 1
    elif '阳' in x:
        return 2
    return 0  
    
def clean_3303(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '阴' in x:
        return 1
    elif '阳' in x:
        return 2
    return 0

def clean_3426(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '黄' in x:
        return 1
    elif '白' in x:
        return 2
    return 0

def clean_3485(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+' in x or '阳' in x or '检出' in x or '查见' in x:
        return 1
    elif '-' in x or '阴' in x or '未' in x:
        return 2
    return 3

def clean_3601(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '正常' in x:
        return 1
    elif '轻度' in x and '少' in x:
        return 2
    elif '中度' in x and '少' in x:
        return 3
    elif '重度' in x and '少' in x:
        return 4
    elif '少' in x:
        return 5
    return 6

def clean_3868(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+' in x or '阳' in x:
        return 1
    elif '-' in x or '阴' in x or '未见' in x:
        return 2
    return 3

def clean_459271(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未见' in x:
        return 0
    elif '建议' in x:
        return 1
    return 2

def clean_A302(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '未' in x:
        return 0
    elif '缺血' in x:
        return 1
    return 2
    
def clean_3191(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '-' in x or '阴' in x:
        return 0
    elif '+' in x or '阳' in x:
        return 1
    return 2
        
def clean_529001(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+++' in x:
        return 0
    elif '++' in x:
        return 1
    elif '++' in x:
        return 2
    return 3

def clean_669016(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+-' in x:
        return 0
    elif '+' in x or '阳' in x:
        return 1
    else:
        return 0

def clean_709039(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '阳' in x or '+' in x:
        return 0
    elif '阴' in x or '-' in x:
        return 1
    return 2
    
def clean_799003(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '++++' in x or '5' in x:
        return 4
    elif '+++' in x or '3' in x:
        return 3
    elif '++' in x or '2' in x:
        return 2
    elif '+' in x or '1+' in x:
        return 1
    else:
        return 0
    
def clean_A49010(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if x == 'Ⅰ':
        return 1
    elif x == 'Ⅱ':
        return 2
    elif x == 'Ⅲ':
        return 3
    elif x == 'Ⅳ':
        return 4
    else:
        return 5
    
    
def clean_A49011(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+' in x or '阳' in x:
        return 1
    elif '++' in x:
        return 2
    elif '+++' in x:
        return 3
    elif '+++' in x:
        return 4
    else:
        return 5  
    
def clean_A705(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '数字化肝超未发现明显异常' in x:
        return 1
    elif '脂肪衰减值大于240' in x:
        return 2
    elif '肝脏脂肪含量超过正常值' in x:
        return 3
    elif '脂肪衰减值越大' in x:
        return 4
    elif '肝脏脂肪含量越高' in x:
        return 5
    elif '提示脂肪肝倾向' in x:
        return 6
    elif '建议定期随诊观察' in x:
        return 7
    elif '经数字化肝超检测' in x:
        return 8
    elif '您的肝脏硬度值偏高' in x:
        return 9
    elif '建议您进行相关的检测和定期随诊观察' in x:
        return 10
    return 11

def clean_E19002(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+++' in x:
        return 3
    elif '++' in x:
        return 2
    elif '+' in x or '阳' in x:
        return 1
    return 4

def clean_E39002(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '3' in x:
        return 3
    elif '2' in x:
        return 2
    elif '1' in x:
        return 1
    elif '阳' in x or '少量' in x:
        return 0
    else:
        return 4
    
def clean_E39003(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '阳' in x:
        return 3
    elif '+++' in x:
        return 2
    elif '++' in x:
        return 1
    elif '未见' in x:
        return 0
    else:
        return 4  
    
def clean_E49029(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if x == 'Ⅳ':
        return 1
    elif x == 'Ⅱ':
        return 2
    elif x == 'Ⅲ':
        return 3
    else:
        return 4
    
def clean_K89001(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '1' in x:
        return 1
    elif '2' in x:
        return 2
    elif '3' in x:
        return 3
    return 4
    
def clean_K89003(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '1+' in x:
        return 1
    elif '2+' in x:
        return 2
    elif '3+' in x:
        return 3
    elif '4+' in x:
        return 4
    else:
        return 5
    
def clean_1001(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '正常' in x:
        return 1
    elif '左偏' in x:
        return 2
    elif '右偏' in x:
        return 3
    elif '过速' in x:
        return 4
    elif '过缓' in x:
        return 5
    elif '改变' in x:
        return 6
    return 7

def clean_2230(x):
    x = str(x)
    if x == "nan":
        return np.NaN
    if '+' in x or '阳' in x:
        return 1
    elif '-' in x or '阴' in x:
        return 2
    return 3
    

    
    
    
    
    
    
    
    
    
    
    


