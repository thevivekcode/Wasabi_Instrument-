
#------------------------EXPERIMENT 2___________------------------------------------------


import matplotlib.pyplot as plt
import numpy as np
import pickle
import pickle

with open("nativePin.pickle",'rb') as handle1:
    pin23=pickle.load(handle1)

with open("output23.pkl",'rb') as handle2:
    wasa23=pickle.load(handle2)



programList =["./datamining/correlation/correlation.c",
"./datamining/covariance/covariance.c",
"./linear-algebra/kernels/2mm/2mm.c",
"./linear-algebra/kernels/3mm/3mm.c",
"./linear-algebra/kernels/atax/atax.c",
"./linear-algebra/kernels/bicg/bicg.c",
"./linear-algebra/kernels/doitgen/doitgen.c",
"./linear-algebra/kernels/mvt/mvt.c",
"./linear-algebra/blas/gemm/gemm.c",
"./linear-algebra/blas/gemver/gemver.c",
"./linear-algebra/blas/gesummv/gesummv.c",
"./linear-algebra/blas/symm/symm.c",
"./linear-algebra/blas/syr2k/syr2k.c",
"./linear-algebra/blas/syrk/syrk.c",
"./linear-algebra/blas/trmm/trmm.c",
"./linear-algebra/solvers/cholesky/cholesky.c",
"./linear-algebra/solvers/durbin/durbin.c",
"./linear-algebra/solvers/gramschmidt/gramschmidt.c",
"./linear-algebra/solvers/lu/lu.c",
"./linear-algebra/solvers/ludcmp/ludcmp.c",
"./linear-algebra/solvers/trisolv/trisolv.c",
"./medley/deriche/deriche.c",
"./medley/floyd-warshall/floyd-warshall.c",
"./medley/nussinov/nussinov.c",
"./stencils/adi/adi.c",
"./stencils/fdtd-2d/fdtd-2d.c",
"./stencils/heat-3d/heat-3d.c",
"./stencils/jacobi-1d/jacobi-1d.c",
"./stencils/jacobi-2d/jacobi-2d.c",
"./stencils/seidel-2d/seidel-2d.c"]


programList1 =["correlation",
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

programList2 =["correlation.c",
"covariance.c",
"2mm.c",
"3mm.c",
"atax.c",
"bicg.c",
"doitgen.c",
"mvt.c",
"gemm.c",
"gemver.c",
"gesummv.c",
"symm.c",
"syr2k.c",
"syrk.c",
"trmm.c",
"cholesky.c",
"durbin.c",
"gramschmidt.c",
"lu.c",
"ludcmp.c",
"trisolv.c",
"deriche.c",
"floyd-warshall.c",
"nussinov.c",
"adi.c",
"fdtd-2d.c",
"heat-3d.c",
"jacobi-1d.c",
"jacobi-2d.c",
"seidel-2d.c"]




optimization=['O0','O1','O2','O3']

for j in optimization:
    dynamicIns=[]
    dynamicIns1=[]


    for i in programList:
        dynamicIns.append(float(pin23[j][i].split()[1]))
    for i in programList2:
        dynamicIns1.append(float(wasa23[j][i].split()[1]))


    import numpy as np
    from matplotlib.pyplot import figure
    n_groups = 30


    figure(num=None, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')
    index = np.arange(n_groups)

    N=30

    ind = np.arange(N)    # the x locations for the groups
    width = 0.3  # the width of the bars: can also be len(x) sequence
    width2 = 0.4
    opacity = 0.8

    rects1 = plt.bar(index, dynamicIns, width,alpha=opacity,color='b',label='NATIVE')
    rects2 = plt.bar(index + width2,dynamicIns1, width,alpha=opacity,color='g',label='WA')

# plt.xlabel('O2 Optimization')

    plt.title('TOTAL DYNAMIC-INSTRUCTION  COMPARISON NATIVE VS WA FOR '+j)
    plt.xticks(index , (programList1), rotation = 'vertical')

    plt.legend((rects1,rects2),("Native","WA"))

    plt.show()
