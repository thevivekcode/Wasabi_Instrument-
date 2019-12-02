# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pickle
from joblib import Parallel, delayed
import multiprocessing
from time import time,sleep
import subprocess
from pprint import pprint

num_cores = multiprocessing.cpu_count()
with open('benchmark_list') as f:
    lines = f.read().splitlines()

pathlist = []
ports = range(8000,8030)
for path in lines:
    pathlist.append(path)
emcc ={}
gcc = {}
def executeGCC(path,optimization):
    temp = ""
    temp+="gcc -"+optimization+" -I ../utilities/ ../utilities/polybench.c ../"+path+" -o "+path.split("/")[-1].replace(".c","")+" -DPOLYBENCH_TIME -lm"
    subprocess.call(temp.split(" "))
    out_file = path.split("/")[-1].replace(".c","")
    temp=subprocess.Popen(["./"+out_file],stdout=subprocess.PIPE)
    temps = temp.communicate()[0]
    temp1=subprocess.call(["rm",out_file])
    print(path.split("/")[-1],temps)
    return (path.split("/")[-1],temps.strip())

def executeBrowser(path,optimization,browser,ports):
    temp =  ""
    parent =  "/".join(path.split("/")[:-1])
    temp+="emcc -"+optimization+" -I ../utilities/ -I"+parent+" ../utilities/polybench.c --emrun -s ALLOW_MEMORY_GROWTH=1 ../"+path+" -o "+path.split("/")[-1].replace(".c",".html")+" -DPOLYBENCH_TIME"

    subprocess.call(temp.split(" "))
    out_file = path.split("/")[-1].replace(".c",".html")
    emrun_call="emrun --browser "+browser+" --port "+str(ports)+" "+out_file
    temp = subprocess.Popen(emrun_call.split(" "),stdout=subprocess.PIPE)
    temps = temp.communicate()[0][:-1].decode("utf-8").split("\n")[-1]
    print(temps)
    temp1 = subprocess.call(["rm",out_file])
    #print(path.split("/")[-1],temps)
    sleep(1)

    return (path.split("/")[-1],temps)

browsers=["firefox","chrome"]
optimizations=["O0", "O1","O2","O3"]
#optimizations=["O3"]
final_output=[]
t=time()

for opt in optimizations:
    print("---------------------------------------------"+opt+"-------------------------------------------")
    gcc[opt]=[]
    res_list = Parallel(n_jobs=num_cores)(delayed(executeGCC)(i,opt) for i in pathlist)

    gcc[opt]=res_list
    print(res_list)
    input_list = zip(pathlist,ports)
    emcc[opt]={}
    emcc[opt]["chrome"]=[]
    emcc[opt]["firefox"]=[]
    sleep(2)

    input_list = zip(pathlist,ports)
    res_list2 = Parallel(n_jobs=num_cores)(delayed(executeBrowser)(path,opt,"firefox",port) for (path,port) in input_list)
    sleep(2)
    emcc[opt]["firefox"]=res_list2
    input_list = zip(pathlist,ports)
    res_list1 = Parallel(n_jobs=num_cores)(delayed(executeBrowser)(path,opt,"chrome",port) for (path,port) in input_list)
    sleep(2)
    emcc[opt]["chrome"]=res_list1
    print(res_list2)


print(time()-t)

pprint(emcc)

out = open(b"emcc.pickle","wb")
pickle.dump(emcc,out)
out.close()

out = open(b"gcc.pickle","wb")
pickle.dump(gcc,out)
out.close()
