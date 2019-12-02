#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:52:31 2019

@author: pratik
"""
import re
import sys
import pickle
from pprint import pprint
file_name = sys.argv[1]
fp = open(file_name,"r")
data= fp.read()
fp.close()
data = re.sub(' +', ' ', data)
data= data.split("\n")
data = data[5:]
final_out = {}
instruction_list=[]
prev_func_number=""
for i in data:
    if 'func' in i and 'function' not in i:
        # print(i)
        func_number = i.split(' ')[1].split('[')[1].split(']')[0]
        final_out[func_number]={}
        final_out[func_number]['base_address']=i.split(' ')[0]
        if prev_func_number!="":
            final_out[prev_func_number]['instructions']=instruction_list
        instruction_list=[]
        prev_func_number= func_number
    else:
        if "local[" in i:
        	continue
        instruction_list.append(i.strip().split(":")[0])
final_out[prev_func_number]['instructions'] =  instruction_list
# pprint(final_out)
fp = open(file_name.replace("txt","pickle"),"wb")
pickle.dump(final_out,fp)
fp.close()
