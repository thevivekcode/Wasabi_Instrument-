from time import time
import os
import subprocess
import pickle
from pprint import pprint
from joblib import Parallel, delayed

num_cores = 1
t =time()
with open('./utilities/benchmark_list') as f:
    lines = f.read().splitlines()
    
gcc=dict()

optimization=["O0", "O1","O2","O3"]

for j in optimization:
	print(j)
	gcc[j]=dict()
	for i in lines:
		print(i)
		gcc[j][i]=""
		gcc1="gcc -"+j+" -I utilities -I" + "/".join(i.split("/")[:-1]) + " utilities/polybench.c "+i+" -o output"+j+" -lm"
		subprocess.call(gcc1.split(" "))
		#os.system(gcc1)
		pin ="./PINF/pin -t ./PINF/source/tools/ManualExamples/obj-intel64/proccount.so -- ./output"+j
		subprocess.call(pin.split(" "))
		#os.system(pin) 
		#gcc[j][i]='\n'.join(str(open("inscount.out").read()).split("\n")[:8])
		gcc[j][i]=str(open("proccount.out").read())
		 
	


#nativePin=Parallel(n_jobs=num_cores)(delayed(pinexec)(i) for i in optimization)
pprint(gcc)
with open('nativePin4.pickle', 'wb') as handle:
    pickle.dump(gcc, handle, protocol=pickle.HIGHEST_PROTOCOL)

print((time()-t)/60)
	
