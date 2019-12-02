from tabulate import tabulate
import pickle
import matplotlib.pyplot as plt

import numpy as np
with open("emcc.pickle",'rb') as handle1:
    emcc =pickle.load(handle1)

with open("gcc.pickle",'rb') as handle2:
    gcc =pickle.load(handle2)


optimization=['O0','O1','O2','O3']

# print("-----------------------------------------GCC VALUE -----------------------------")
gccO0= [float(X[1]) for X in gcc["O0"]] #gcc value for O0 optimization
gccO1= [float(X[1]) for X in gcc["O1"]]
gccO2= [float(X[1]) for X in gcc["O2"]]
gccO3= [float(X[1]) for X in gcc["O3"]]

# print(gccO0,"\n",gccO1,"\n",gccO2,"\n",gccO3)

# print("-----------------------------------------EMCC VALUE -----------------------------")
emcc_chrome_O0 =[float(X[1]) for X in emcc["O0"]["chrome"]]
emcc_firefox_O0 =[float(X[1]) for X in emcc["O0"]["firefox"]]
emcc_chrome_O1 =[float(X[1]) for X in emcc["O1"]["chrome"]]
emcc_firefox_O1 =[float(X[1]) for X in emcc["O1"]["firefox"]]
emcc_chrome_O2 =[float(X[1]) for X in emcc["O2"]["chrome"]]
emcc_firefox_O2 =[float(X[1]) for X in emcc["O2"]["firefox"]]
emcc_chrome_O3 =[float(X[1]) for X in emcc["O3"]["chrome"]]
emcc_firefox_O3 =[float(X[1]) for X in emcc["O3"]["firefox"]]

files =["correlation",
"covariance",
"2mm",
"3mm",
"atax",
"bicg",
"doitgen",
"mvt",
"gemm",
"gemver",
"gesummv",
"symm",
"syr2k",
"syrk",
"trmm",
"cholesky",
"durbin",
"gramschmidt",
"lu",
"ludcmp",
"trisolv",
"deriche",
"floyd-warshall",
"nussinov",
"adi",
"fdtd-2d",
"heat-3d",
"jacobi-1d",
"jacobi-2d",
"seidel-2d"]

data = []
for index,i in enumerate(emcc_chrome_O3):
    t1 = []
    t1.append(files[index])
    t1.append(gccO3[index])
    t1.append(i)
    t1.append(emcc_firefox_O3[index])
    data.append(t1)

titles=["FileName","Native","Chrome","Firefox"]
'''
print('|{:<6}\t\t|{:<6}\t\t|{:<6}\t\t|{:<6}|'.format(*titles))
for item in zip(files, gccO0, emcc_chrome_O0, emcc_firefox_O0):
    print('|{:<6}\t\t|{:<6}\t\t|{:<6}\t\t|{:<6}|'.format(*item))
'''
columns = titles
n_rows = len(files)
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(files)))
y_offset = np.zeros(len(titles))
cell_text = []
temp = np.array(data)
'''
for row in range(n_rows):
    y_offset = y_offset + data[row]
    cell_text.append([x for x in y_offset])
cell_text.reverse()
'''
fig, axs =plt.subplots(2,1)
axs[0].axis('tight')
axs[0].axis('off')
# plt.table(cellText=data,
#                       rowColours=colors,
#                       colLabels=columns,loc='center')
table = axs[0].table(cellText=temp,colLabels=columns,loc='center')

table.scale(0.8,0.5)
# axs[1].plot(temp[:,0],temp[:,1])
plt.axis('off')
plt.show()
