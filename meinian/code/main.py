# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:07:36 2018

@author: Administrator
"""

import _0_data_transform
import _1_data_clean
import _2_data_clean
import _3_1_data_split_1
import _3_2_data_numer
import _3_3_data_txt_1
import _3_3_data_txt_2
import _4_1_lgb

print("=============step0==============")
_0_data_transform.step_0()
print("=============step1==============")
_1_data_clean.step_1()
print("=============step2==============")
_2_data_clean.step_2()
print("=============step3==============")
_3_1_data_split_1.step_3()
print("=============step4==============")
_3_2_data_numer.step_4()
print("=============step5==============")
_3_3_data_txt_1.step_5()
print("=============step6==============")
_3_3_data_txt_2.step_6()
print("=============step7==============")
_4_1_lgb.step_7()
print("=============over==============")
