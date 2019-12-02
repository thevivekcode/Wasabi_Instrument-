# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
from pprint import pprint
import json
import subprocess
from collections import OrderedDict
with open('benchmark_list') as f:
    lines = f.read().splitlines()
pathlist = []
for path in lines:
    pathlist.append(path)

def fetchFunctionName(cFile,optimization,function_number):
    first_parameter = cFile.replace(".c","")
    second_parameter = optimization
    third_parameter = str(function_number)
    temp = subprocess.Popen(["sh","func_name.sh",first_parameter,second_parameter,third_parameter],stdout=subprocess.PIPE)
    file_name = temp.communicate()[0].decode("utf-8")
    return file_name
    

parse_file = open("wasabi_O3.pkl","rb")
data = pickle.load(parse_file)
question23 = {}
question4 = {}
flag=0
mapping = {"branch":"BranchCount","float":"Float","integer":"Integer","load":"LoadCount","register":"RegisterCount","store":"StoreCOunt","total_count":"DynamicCount","nop":"NOPcount"}
for k1,v1 in data.items():

    temp = data[k1]['firefox']
    question23[k1]={}
    question4[k1]={}
    for j in temp:
        tool = j
                
        filename=j[0].strip()
        optimization = k1
        ques4={}
        print(filename)        
        
        question23[optimization][filename]=""
        question4[optimization][filename]=""
        count_data ='{ "exp2and3'+ tool[1].decode("utf-8").split("html")[1].strip().replace("\n","").replace("\\n","").replace("\\","").split("exp2and3")[-1]
        count_data = json.loads(count_data.replace('"{','{').replace('}"','}'))
        temp_arr = dict(OrderedDict(sorted(count_data['exp4'].items(), key=lambda x: x[1],reverse=True)))
        count_data['exp4']=temp_arr
        for k,v in mapping.items():
            if k not in count_data["exp2and3"]:
                count_data["exp2and3"][k]=0;
        for key,value in count_data.items():
            if(key=='exp2and3'):
                for k,v in value.items():
                    question23[optimization][filename]+=mapping[k]+" "+str(v)+"\n"
            if(key=='exp4new'):
                temp_str = ""
                a = 0
                other_count=0
                total_count = 0
                for k,v in count_data["exp4"].items():
                    total_count+=count_data["exp4new"][k]
                for k,v in count_data["exp4"].items():
                    if(a>3):
                        other_count+=count_data["exp4new"][k]/total_count
                    else:
                        temp_str+=k+" "+str(count_data["exp4new"][k]/total_count)+"\n"
                    a+=1
                temp_str+="Others "+str(other_count)+"\n"
                question4[optimization][filename]=temp_str

parse_file.close()
file = open("output23.pkl","wb")
pickle.dump(question23,file)
file.close()

file = open("output4.pkl","wb")
pickle.dump(question4,file)
file.close()
