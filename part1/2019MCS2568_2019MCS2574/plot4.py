
import matplotlib.pyplot as plt
import numpy as np
import pickle

with open("nativePin4.pickle","rb") as handle1:
    PINX=pickle.load(handle1)

with open("output4.pkl","rb") as handle2:
    WAX=pickle.load(handle2)



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

#print(PINX["O0"]["./stencils/seidel-2d/seidel-2d.c"])
# strr=PINX["O0"]["./stencils/seidel-2d/seidel-2d.c"].split()[1]
#print(strr.split())

optimization=['O0','O1','O2','O3']

for j in optimization:

    list1=[]
    list2=[]
    list3=[]
    list4=[]
    listOthers=[]
    list1W=[]
    list2W=[]
    list3W=[]
    list4W=[]
    listOthersW=[]
    for i in programList:
        list1.append(float(PINX["O0"][i].split()[1]))
        list2.append(float(PINX["O0"][i].split()[3]))
        list3.append(float(PINX["O0"][i].split()[5]))
        list4.append(float(PINX["O0"][i].split()[7]))
        listOthers.append(float(PINX["O0"][i].split()[9]))

    for i in programList2:
        list1W.append(float(WAX["O0"][i].split()[1]))
        list2W.append(float(WAX["O0"][i].split()[3]))
        list3W.append(float(WAX["O0"][i].split()[5]))
        list4W.append(float(WAX["O0"][i].split()[7]))
        listOthersW.append(float(WAX["O0"][i].split()[9]))



    import numpy as np
    from matplotlib.pyplot import figure
    n_groups = 30

    # create plot
    # fig, ax = plt.subplots()
    figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')
    index = np.arange(n_groups)

    N=30
    x=2**(-N)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35 # the width of the bars: can also be len(x) sequence
    width2 = 0.4
    p1 = plt.bar(ind, list1, width,color='blue')
    p2 = plt.bar(ind, list2, width,bottom=list1,color='orange')
    x=np.add(list1,list2)
    p3 = plt.bar(ind, list3, width,bottom=x,color='green')
    x1=np.add(x,list3)
    p4 = plt.bar(ind, list4, width,bottom=x1,color='grey')
    x2=np.add(x1,list4)
    p5 = plt.bar(ind, listOthers, width,bottom=x2,color='#81930A')



    p6 = plt.bar(ind+width2, list1W, width,color='blue')
    p7 = plt.bar(ind+width2, list2W, width,bottom=list1W,color='orange')
    x=np.add(list1W,list2W)
    p8 = plt.bar(ind+width2, list3W, width,bottom=x,color='green')
    x1=np.add(x,list3W)
    p9 = plt.bar(ind+width2, list4W, width,bottom=x1,color='grey')
    x2=np.add(x1,list4W)
    p10 = plt.bar(ind+width2, listOthersW, width,bottom=x2,color='#81930A')


    plt.yscale('log',basey=2)
    plt.title('HOT CODE AND ITS INSTRUCTION COUNT FOR OPTIMIZATION '+j)
    plt.xticks(index , (programList1), rotation = 'vertical')
    #plt.yticks(np.arange(0,1.1,.0001))
    plt.legend((p1[0], p2[0],p3[0],p4[0],p5[0],p6[0], p7[0],p8[0],p9[0],p10[0]), ('I-native','II-native','III-native','IV-native','Others-native','I-WA','II-WA','III-WA','IV-WA','Others-WA'))

    plt.show()
