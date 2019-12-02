#Final value is processed here
# experiment 1::

import matplotlib.pyplot as plt
import numpy as np
import pickle

with open("emcc.pickle",'rb') as handle1:
    emcc =pickle.load(handle1)

with open("gcc.pickle",'rb') as handle2:
    gcc =pickle.load(handle2)




# emcc ={'O0': {'chrome': [('correlation.c', '0.385000'),
#                    ('covariance.c', '0.353000'),
#                    ('2mm.c', '0.166000'),
#                    ('3mm.c', '0.191000'),
#                    ('atax.c', '0.042000'),
#                    ('bicg.c', '0.033000'),
#                    ('doitgen.c', '2.822000'),
#                    ('mvt.c', '0.076000'),
#                    ('gemm.c', '0.087000'),
#                    ('gemver.c', '0.102000'),
#                    ('gesummv.c', '0.012000'),
#                    ('symm.c', '0.052000'),
#                    ('syr2k.c', '0.145000'),
#                    ('syrk.c', '0.037000'),
#                    ('trmm.c', '0.024000'),
#                    ('cholesky.c', '0.057000'),
#                    ('durbin.c', '0.024000'),
#                    ('gramschmidt.c', '0.068000'),
#                    ('lu.c', '0.164000'),
#                    ('ludcmp.c', '0.140000'),
#                    ('trisolv.c', '0.010000'),
#                    ('deriche.c', '1.152000'),
#                    ('nussinov.c', '0.165000'),
#                    ('floyd-warshall.c', '0.722000'),
#                    ('adi.c', '0.233000'),
#                    ('fdtd-2d.c', '0.133000'),
#                    ('heat-3d.c', '0.188000'),
#                    ('jacobi-1d.c', '0.010000'),
#                    ('jacobi-2d.c', '0.092000'),
#                    ('seidel-2d.c', '0.322000')],
#         'firefox': [('correlation.c', '0.238000'),
#                     ('covariance.c', '0.240000'),
#                     ('2mm.c', '0.100000'),
#                     ('3mm.c', '0.131000'),
#                     ('atax.c', '0.037000'),
#                     ('bicg.c', '0.033000'),
#                     ('doitgen.c', '2.975000'),
#                     ('mvt.c', '0.074000'),
#                     ('gemm.c', '0.034000'),
#                     ('gemver.c', '0.097000'),
#                     ('gesummv.c', '0.014000'),
#                     ('symm.c', '0.032000'),
#                     ('syr2k.c', '0.094000'),
#                     ('syrk.c', '0.028000'),
#                     ('trmm.c', '0.026000'),
#                     ('cholesky.c', '0.050000'),
#                     ('durbin.c', '0.031000'),
#                     ('gramschmidt.c', '0.066000'),
#                     ('lu.c', '0.112000'),
#                     ('ludcmp.c', '0.131000'),
#                     ('trisolv.c', '0.013000'),
#                     ('deriche.c', '0.688000'),
#                     ('nussinov.c', '0.088000'),
#                     ('floyd-warshall.c', '0.544000'),
#                     ('adi.c', '0.175000'),
#                     ('fdtd-2d.c', '0.082000'),
#                     ('heat-3d.c', '0.098000'),
#                     ('jacobi-1d.c', '0.011000'),
#                     ('jacobi-2d.c', '0.079000'),
#                     ('seidel-2d.c', '0.306000')]},
#  'O1': {'chrome': [('correlation.c', '0.284000'),
#                    ('covariance.c', '0.269000'),
#                    ('2mm.c', '0.116000'),
#                    ('3mm.c', '0.177000'),
#                    ('atax.c', '0.036000'),
#                    ('bicg.c', '0.019000'),
#                    ('doitgen.c', '2.687000'),
#                    ('mvt.c', '0.049000'),
#                    ('gemm.c', '0.059000'),
#                    ('gemver.c', '0.135000'),
#                    ('gesummv.c', '0.011000'),
#                    ('symm.c', '0.044000'),
#                    ('syr2k.c', '0.328000'),
#                    ('syrk.c', '0.033000'),
#                    ('trmm.c', '0.047000'),
#                    ('cholesky.c', '0.120000'),
#                    ('durbin.c', '0.018000'),
#                    ('gramschmidt.c', '0.075000'),
#                    ('lu.c', '0.220000'),
#                    ('ludcmp.c', '0.067000'),
#                    ('trisolv.c', '0.014000'),
#                    ('deriche.c', '0.951000'),
#                    ('nussinov.c', '0.135000'),
#                    ('floyd-warshall.c', '0.465000'),
#                    ('adi.c', '0.402000'),
#                    ('fdtd-2d.c', '0.170000'),
#                    ('heat-3d.c', '0.114000'),
#                    ('jacobi-1d.c', '0.009000'),
#                    ('jacobi-2d.c', '0.047000'),
#                    ('seidel-2d.c', '0.267000')],
#         'firefox': [('correlation.c', '0.321000'),
#                     ('covariance.c', '0.175000'),
#                     ('2mm.c', '0.068000'),
#                     ('3mm.c', '0.120000'),
#                     ('atax.c', '0.038000'),
#                     ('bicg.c', '0.039000'),
#                     ('doitgen.c', '2.848000'),
#                     ('mvt.c', '0.044000'),
#                     ('gemm.c', '0.088000'),
#                     ('gemver.c', '0.091000'),
#                     ('gesummv.c', '0.009000'),
#                     ('symm.c', '0.034000'),
#                     ('syr2k.c', '0.084000'),
#                     ('syrk.c', '0.015000'),
#                     ('trmm.c', '0.031000'),
#                     ('cholesky.c', '0.055000'),
#                     ('durbin.c', '0.032000'),
#                     ('gramschmidt.c', '0.053000'),
#                     ('lu.c', '0.127000'),
#                     ('ludcmp.c', '0.108000'),
#                     ('trisolv.c', '0.013000'),
#                     ('deriche.c', '0.639000'),
#                     ('nussinov.c', '0.120000'),
#                     ('floyd-warshall.c', '0.401000'),
#                     ('adi.c', '0.181000'),
#                     ('fdtd-2d.c', '0.078000'),
#                     ('heat-3d.c', '0.101000'),
#                     ('jacobi-1d.c', '0.008000'),
#                     ('jacobi-2d.c', '0.103000'),
#                     ('seidel-2d.c', '0.256000')]},
#  'O2': {'chrome': [('correlation.c', '0.163000'),
#                    ('covariance.c', '0.151000'),
#                    ('2mm.c', '0.074000'),
#                    ('3mm.c', '0.119000'),
#                    ('atax.c', '0.027000'),
#                    ('bicg.c', '0.022000'),
#                    ('doitgen.c', '1.128000'),
#                    ('mvt.c', '0.108000'),
#                    ('gemm.c', '0.049000'),
#                    ('gemver.c', '0.347000'),
#                    ('gesummv.c', '0.010000'),
#                    ('symm.c', '0.059000'),
#                    ('syr2k.c', '0.200000'),
#                    ('syrk.c', '0.087000'),
#                    ('trmm.c', '0.063000'),
#                    ('cholesky.c', '0.038000'),
#                    ('durbin.c', '0.041000'),
#                    ('gramschmidt.c', '0.092000'),
#                    ('lu.c', '0.230000'),
#                    ('ludcmp.c', '0.116000'),
#                    ('trisolv.c', '0.007000'),
#                    ('deriche.c', '2.513000'),
#                    ('nussinov.c', '0.141000'),
#                    ('floyd-warshall.c', '0.655000'),
#                    ('adi.c', '0.218000'),
#                    ('fdtd-2d.c', '0.074000'),
#                    ('heat-3d.c', '0.115000'),
#                    ('jacobi-1d.c', '0.020000'),
#                    ('jacobi-2d.c', '0.084000'),
#                    ('seidel-2d.c', '0.347000')],
#         'firefox': [('correlation.c', '0.467000'),
#                     ('covariance.c', '0.148000'),
#                     ('2mm.c', '0.074000'),
#                     ('3mm.c', '0.058000'),
#                     ('atax.c', '0.051000'),
#                     ('bicg.c', '0.020000'),
#                     ('doitgen.c', '1.440000'),
#                     ('mvt.c', '0.048000'),
#                     ('gemm.c', '0.030000'),
#                     ('gemver.c', '0.095000'),
#                     ('gesummv.c', '0.014000'),
#                     ('symm.c', '0.042000'),
#                     ('syr2k.c', '0.126000'),
#                     ('syrk.c', '0.020000'),
#                     ('trmm.c', '0.035000'),
#                     ('cholesky.c', '0.045000'),
#                     ('durbin.c', '0.020000'),
#                     ('gramschmidt.c', '0.057000'),
#                     ('lu.c', '0.073000'),
#                     ('ludcmp.c', '0.245000'),
#                     ('trisolv.c', '0.009000'),
#                     ('deriche.c', '1.154000'),
#                     ('nussinov.c', '0.163000'),
#                     ('floyd-warshall.c', '0.510000'),
#                     ('adi.c', '0.162000'),
#                     ('fdtd-2d.c', '0.087000'),
#                     ('heat-3d.c', '0.173000'),
#                     ('jacobi-1d.c', '0.015000'),
#                     ('jacobi-2d.c', '0.068000'),
#                     ('seidel-2d.c', '0.256000')]},
#  'O3': {'chrome': [('correlation.c', '0.161000'),
#                    ('covariance.c', '0.201000'),
#                    ('2mm.c', '0.049000'),
#                    ('3mm.c', '0.129000'),
#                    ('atax.c', '0.031000'),
#                    ('bicg.c', '0.025000'),
#                    ('doitgen.c', '1.344000'),
#                    ('mvt.c', '0.196000'),
#                    ('gemm.c', '0.041000'),
#                    ('gemver.c', '0.081000'),
#                    ('gesummv.c', '0.009000'),
#                    ('symm.c', '0.144000'),
#                    ('syr2k.c', '0.128000'),
#                    ('syrk.c', '0.035000'),
#                    ('trmm.c', '0.046000'),
#                    ('cholesky.c', '0.035000'),
#                    ('durbin.c', '0.069000'),
#                    ('gramschmidt.c', '0.142000'),
#                    ('lu.c', '0.112000'),
#                    ('ludcmp.c', '0.165000'),
#                    ('trisolv.c', '0.025000'),
#                    ('deriche.c', '0.867000'),
#                    ('nussinov.c', '0.225000'),
#                    ('floyd-warshall.c', '0.709000'),
#                    ('adi.c', '0.139000'),
#                    ('fdtd-2d.c', '0.335000'),
#                    ('heat-3d.c', '0.104000'),
#                    ('jacobi-1d.c', '0.005000'),
#                    ('jacobi-2d.c', '0.044000'),
#                    ('seidel-2d.c', '0.263000')],
#         'firefox': [('correlation.c', '0.320000'),
#                     ('covariance.c', '0.121000'),
#                     ('2mm.c', '0.041000'),
#                     ('3mm.c', '0.058000'),
#                     ('atax.c', '0.035000'),
#                     ('bicg.c', '0.020000'),
#                     ('doitgen.c', '1.542000'),
#                     ('mvt.c', '0.039000'),
#                     ('gemm.c', '0.054000'),
#                     ('gemver.c', '0.083000'),
#                     ('gesummv.c', '0.009000'),
#                     ('symm.c', '0.047000'),
#                     ('syr2k.c', '0.158000'),
#                     ('syrk.c', '0.066000'),
#                     ('trmm.c', '0.028000'),
#                     ('cholesky.c', '0.060000'),
#                     ('durbin.c', '0.028000'),
#                     ('gramschmidt.c', '0.069000'),
#                     ('lu.c', '0.099000'),
#                     ('ludcmp.c', '0.121000'),
#                     ('trisolv.c', '0.009000'),
#                     ('deriche.c', '0.637000'),
#                     ('nussinov.c', '0.120000'),
#                     ('floyd-warshall.c', '0.540000'),
#                     ('adi.c', '0.163000'),
#                     ('fdtd-2d.c', '0.066000'),
#                     ('heat-3d.c', '0.150000'),
#                     ('jacobi-1d.c', '0.012000'),
#                     ('jacobi-2d.c', '0.066000'),
#                     ('seidel-2d.c', '0.255000')]}}
#
# #-----------------------------------------------------------------------------------------------------------------
#
# gcc = {'O0': [('correlation.c', b'1.036447'),
#         ('covariance.c', b'1.023256'),
#         ('2mm.c', b'0.217544'),
#         ('3mm.c', b'0.294644'),
#         ('atax.c', b'0.067357'),
#         ('bicg.c', b'0.094306'),
#         ('doitgen.c', b'9.053019'),
#         ('mvt.c', b'0.115363'),
#         ('gemm.c', b'0.142328'),
#         ('gemver.c', b'0.203771'),
#         ('gesummv.c', b'0.039934'),
#         ('symm.c', b'0.234910'),
#         ('syr2k.c', b'0.452390'),
#         ('syrk.c', b'0.128161'),
#         ('trmm.c', b'0.120602'),
#         ('cholesky.c', b'0.180052'),
#         ('durbin.c', b'0.038307'),
#         ('gramschmidt.c', b'0.204757'),
#         ('lu.c', b'0.629148'),
#         ('ludcmp.c', b'0.311057'),
#         ('trisolv.c', b'0.018677'),
#         ('deriche.c', b'1.700097'),
#         ('nussinov.c', b'0.435825'),
#         ('floyd-warshall.c', b'2.190420'),
#         ('adi.c', b'0.890928'),
#         ('fdtd-2d.c', b'0.421735'),
#         ('heat-3d.c', b'1.002170'),
#         ('jacobi-1d.c', b'0.023774'),
#         ('jacobi-2d.c', b'0.242640'),
#         ('seidel-2d.c', b'0.494345')],
#  'O1': [('correlation.c', b'0.314698'),
#         ('covariance.c', b'0.437110'),
#         ('2mm.c', b'0.101363'),
#         ('3mm.c', b'0.125874'),
#         ('atax.c', b'0.031783'),
#         ('bicg.c', b'0.021720'),
#         ('doitgen.c', b'3.046613'),
#         ('mvt.c', b'0.049865'),
#         ('gemm.c', b'0.033279'),
#         ('gemver.c', b'0.066835'),
#         ('gesummv.c', b'0.010057'),
#         ('symm.c', b'0.029800'),
#         ('syr2k.c', b'0.060021'),
#         ('syrk.c', b'0.026625'),
#         ('trmm.c', b'0.026329'),
#         ('cholesky.c', b'0.065887'),
#         ('durbin.c', b'0.033482'),
#         ('gramschmidt.c', b'0.086720'),
#         ('lu.c', b'0.113472'),
#         ('ludcmp.c', b'0.055540'),
#         ('trisolv.c', b'0.010583'),
#         ('deriche.c', b'0.691137'),
#         ('nussinov.c', b'0.122582'),
#         ('floyd-warshall.c', b'0.325597'),
#         ('adi.c', b'0.200365'),
#         ('fdtd-2d.c', b'0.074208'),
#         ('heat-3d.c', b'0.096660'),
#         ('jacobi-1d.c', b'0.002308'),
#         ('jacobi-2d.c', b'0.033601'),
#         ('seidel-2d.c', b'0.300143')],
#  'O2': [('correlation.c', b'0.231351'),
#         ('covariance.c', b'0.225220'),
#         ('2mm.c', b'0.045797'),
#         ('3mm.c', b'0.081769'),
#         ('atax.c', b'0.037178'),
#         ('bicg.c', b'0.020807'),
#         ('doitgen.c', b'1.689575'),
#         ('mvt.c', b'0.038663'),
#         ('gemm.c', b'0.025122'),
#         ('gemver.c', b'0.052417'),
#         ('gesummv.c', b'0.009474'),
#         ('symm.c', b'0.044210'),
#         ('syr2k.c', b'0.066058'),
#         ('syrk.c', b'0.015268'),
#         ('trmm.c', b'0.022573'),
#         ('cholesky.c', b'0.032887'),
#         ('durbin.c', b'0.009279'),
#         ('gramschmidt.c', b'0.042037'),
#         ('lu.c', b'0.082995'),
#         ('ludcmp.c', b'0.044794'),
#         ('trisolv.c', b'0.005267'),
#         ('deriche.c', b'0.633365'),
#         ('nussinov.c', b'0.109430'),
#         ('floyd-warshall.c', b'0.308352'),
#         ('adi.c', b'0.188833'),
#         ('fdtd-2d.c', b'0.063153'),
#         ('heat-3d.c', b'0.091511'),
#         ('jacobi-1d.c', b'0.004531'),
#         ('jacobi-2d.c', b'0.032148'),
#         ('seidel-2d.c', b'0.297752')],
#  'O3': [('correlation.c', b'0.162554'),
#         ('covariance.c', b'0.204879'),
#         ('2mm.c', b'0.079362'),
#         ('3mm.c', b'0.086416'),
#         ('atax.c', b'0.016999'),
#         ('bicg.c', b'0.021131'),
#         ('doitgen.c', b'1.794551'),
#         ('mvt.c', b'0.080292'),
#         ('gemm.c', b'0.011829'),
#         ('gemver.c', b'0.054802'),
#         ('gesummv.c', b'0.009787'),
#         ('symm.c', b'0.034428'),
#         ('syr2k.c', b'0.104220'),
#         ('syrk.c', b'0.016662'),
#         ('trmm.c', b'0.013661'),
#         ('cholesky.c', b'0.025218'),
#         ('durbin.c', b'0.007197'),
#         ('gramschmidt.c', b'0.038742'),
#         ('lu.c', b'0.091777'),
#         ('ludcmp.c', b'0.055867'),
#         ('trisolv.c', b'0.007480'),
#         ('deriche.c', b'0.586128'),
#         ('nussinov.c', b'0.108747'),
#         ('floyd-warshall.c', b'0.289256'),
#         ('adi.c', b'0.195417'),
#         ('fdtd-2d.c', b'0.033311'),
#         ('heat-3d.c', b'0.081371'),
#         ('jacobi-1d.c', b'0.002757'),
#         ('jacobi-2d.c', b'0.061438'),
#         ('seidel-2d.c', b'0.251114')]}
#-----------------------------------Above data is used to build below bar-graph-----------------------------

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

# print(emcc_chrome_O0,"\n",emcc_firefox_O0,"\n",emcc_chrome_O1,"\n",emcc_firefox_O1,"\n",emcc_chrome_O2,"\n",emcc_firefox_O2,"\n",emcc_chrome_O3,"\n",emcc_firefox_O3)

print("-----------------------------------------Relative VALUE -----------------------------")
for i in range(30):
    emcc_chrome_O0[i]/= gccO0[i]
    emcc_firefox_O0[i]/=gccO0[i]
    emcc_chrome_O1[i]/= gccO1[i]
    emcc_firefox_O1[i]/=gccO1[i]
    emcc_chrome_O2[i]/= gccO2[i]
    emcc_firefox_O2[i]/=gccO2[i]
    emcc_chrome_O3[i]/= gccO3[i]
    emcc_firefox_O3[i]/=gccO3[i]

n_groups = 30
#-------------------------------------------GRAPH_PLOT--------------------------------------------------
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

programList =["correlation",
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

rects1 = plt.bar(index, emcc_chrome_O0, bar_width,
alpha=opacity,
color='b',
label='EMCC_CHROME')

rects2 = plt.bar(index + bar_width,emcc_firefox_O0, bar_width,
alpha=opacity,
color='g',
label='EMCC_FIREFOX')

plt.xlabel('O0 Optimization')
plt.ylabel('Time')
plt.title('Native vs WA in Different Browser')
plt.xticks(index + bar_width, (programList), rotation = 'vertical')
plt.legend()
plt.axhline(y=1, color='r', linestyle='-')
plt.tight_layout()
plt.show()

#---------------------------------------------second-----------------------------------------------

rects1 = plt.bar(index, emcc_chrome_O1, bar_width,
alpha=opacity,
color='b',
label='EMCC_CHROME')

rects2 = plt.bar(index + bar_width,emcc_firefox_O1, bar_width,
alpha=opacity,
color='g',
label='EMCC_FIREFOX')

plt.xlabel('O1 Optimization')
plt.ylabel('Time')
plt.title('Native vs WA in Different Browser')
plt.xticks(index + bar_width, (programList), rotation = 'vertical')
plt.legend()
plt.axhline(y=1, color='r', linestyle='-')
plt.tight_layout()
plt.show()

#---------------------------------------------third-----------------------------------------------

rects1 = plt.bar(index, emcc_chrome_O2, bar_width,
alpha=opacity,
color='b',
label='EMCC_CHROME')

rects2 = plt.bar(index + bar_width,emcc_firefox_O2, bar_width,
alpha=opacity,
color='g',
label='EMCC_FIREFOX')

plt.xlabel('O2 Optimization')
plt.ylabel('Time')
plt.title('Native vs WA in Different Browser')
plt.xticks(index + bar_width, (programList), rotation = 'vertical')
plt.legend()
plt.axhline(y=1, color='r', linestyle='-')
plt.tight_layout()
plt.show()

#---------------------------------------------fourth-----------------------------------------------

rects1 = plt.bar(index, emcc_chrome_O3, bar_width,
alpha=opacity,
color='b',
label='EMCC_CHROME')

rects2 = plt.bar(index + bar_width,emcc_firefox_O3, bar_width,
alpha=opacity,
color='g',
label='EMCC_FIREFOX')

plt.xlabel('O3 Optimization')
plt.ylabel('Time')
plt.title('Native vs WA in Different Browser')
plt.xticks(index + bar_width, (programList), rotation = 'vertical')
plt.legend()
plt.axhline(y=1, color='r', linestyle='-')
plt.tight_layout()
plt.show()
