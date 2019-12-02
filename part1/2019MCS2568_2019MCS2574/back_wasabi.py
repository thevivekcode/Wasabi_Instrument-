# -*- coding: utf-8 -*-
import os
from joblib import Parallel, delayed
import multiprocessing
from time import time,sleep
import subprocess
from pprint import pprint
import pickle
import json

num_cores = multiprocessing.cpu_count()
with open('benchmark_list') as f:
    lines = f.read().splitlines()
pathlist = []
ports = range(7000,7030)
for path in lines:
    pathlist.append(path)
wasabi={}
#Controller Function that runs wasabiCommands.sh and creates the .html file and then runs emrun such that after the execution is complete
#we get output JSON on console which we send as a tuple along with file name.
def wasabiController(path,optimization,browser,ports):
    first_parameter = optimization
    second_parameter =  "/".join(path.split("/")[:-1])
    third_parameter = path
    fourth_parameter = path.split("/")[-1].replace(".c","")+"_"+optimization
    fifth_parameter = "instruction-mix.js"
    sixth_parameter = str(ports)
    seventh_parameter = browser
    print(first_parameter)
    print(second_parameter)
    print(third_parameter)
    print(fourth_parameter)
    print(fifth_parameter)
    print(sixth_parameter)
    print(seventh_parameter)

    temp = subprocess.call(["sh","wasabiCommands.sh",first_parameter,second_parameter,third_parameter,fourth_parameter,fifth_parameter])
    output = subprocess.Popen(["emrun","--browser",seventh_parameter,"--port",sixth_parameter,fourth_parameter+".html"],stdout=subprocess.PIPE)
    output_dat = output.communicate()[0]
    return (path.split("/")[-1],output_dat)


browsers=["firefox"]
optimizations=["O1","O0","O2","O3"]
final_output=[]
t=time()
for opt in optimizations:
    wasabi[opt]={}
    print("---------------------------------------------"+opt+"-------------------------------------------")
    for b in browsers:
        wasabi[opt][b]=[]
        input_list = zip(pathlist,ports)
        #Initializing threads = number of cores = 4 in our case. 
        res_list1 = Parallel(n_jobs=num_cores)(delayed(wasabiController)(path,opt,b,port) for (path,port) in input_list)
        wasabi[opt][b]=res_list1
	#Sleep done to ensure synchronization between creating 2 thread processes.
        sleep(2)
    temp = "wasabi_"+opt+".pkl";
    out = open(temp,"wb")
    pickle.dump(wasabi,out)#Output file is pickled and is then used in other python scripts to generate graphs using matplotlib
    out.close()
    print(res_list1)


print(time()-t)
