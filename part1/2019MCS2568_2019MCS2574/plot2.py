
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
    load=[]
    store=[]
    Int=[]
    Float=[]
    Branch=[]
    Register=[]
    Nop=[]

    load1=[]
    store1=[]
    Int1=[]
    Float1=[]
    Branch1=[]
    Register1=[]
    Nop1=[]


    for i in programList:
        load.append(float(pin23[j][i].split()[3])/float(pin23[j][i].split()[1]))
        store.append(float(pin23[j][i].split()[5])/float(pin23[j][i].split()[1]))
        Int.append(float(pin23[j][i].split()[7])/float(pin23[j][i].split()[1]))
        Float.append(float(pin23[j][i].split()[9])/float(pin23[j][i].split()[1]))
        Branch.append(float(pin23[j][i].split()[11])/float(pin23[j][i].split()[1]))
        Register.append(float(pin23[j][i].split()[13])/float(pin23[j][i].split()[1]))
        Nop.append(float(pin23[j][i].split()[15])/float(pin23[j][i].split()[1]))

    for i in programList2:
        if(float(wasa23[j][i].split()[1])<0):
        	wasa23[j][i].split()[1]=float(wasa23[j][i].split()[1])*-1
        load1.append(float(wasa23[j][i].split()[9])/float(wasa23[j][i].split()[1]))
        store1.append(float(wasa23[j][i].split()[15])/float(wasa23[j][i].split()[1]))
        Int1.append(float(wasa23[j][i].split()[11])/float(wasa23[j][i].split()[1]))
        Float1.append(float(wasa23[j][i].split()[7])/float(wasa23[j][i].split()[1]))
        Branch1.append(float(wasa23[j][i].split()[13])/float(wasa23[j][i].split()[1]))
        if(float(wasa23[j][i].split()[3])/float(wasa23[j][i].split()[1])<0):
        	Register1.append(float(wasa23[j][i].split()[3])/float(wasa23[j][i].split()[1])*-1)
        else:
        	Register1.append(float(wasa23[j][i].split()[3])/float(wasa23[j][i].split()[1]))
        Nop1.append(float(wasa23[j][i].split()[5])/float(wasa23[j][i].split()[1]))


    # print(load)
    # print(store)
    # print(Int)
    # print(Float)
    # print(Branch)
    # print(Register)
    # print(Nop)

    import numpy as np
    from matplotlib.pyplot import figure
    n_groups = 30

    # create plot
    # fig, ax = plt.subplots()
    figure(num=None, figsize=(20, 10), dpi=80, facecolor='w', edgecolor='k')
    index = np.arange(n_groups)

    N=30

    ind = np.arange(N)    # the x locations for the groups
    width = 0.3  # the width of the bars: can also be len(x) sequence
    width2 = 0.4
    p1 = plt.bar(ind, load, width,color='blue')
    p2 = plt.bar(ind, store, width,bottom=load,color='orange')
    x=np.add(load,store)
    p3 = plt.bar(ind, Int, width,bottom=x,color='green')
    x1=np.add(x,Int)
    p4 = plt.bar(ind, Float, width,bottom=x1,color='grey')
    x2=np.add(x1,Float)
    p5 = plt.bar(ind, Branch, width,bottom=x2,color='purple')
    x3=np.add(x2,Branch)
    p6 = plt.bar(ind, Register, width,bottom=x3,color='#1BCE4B')
    x4=np.add(x3,Register)
    p7 = plt.bar(ind, Nop, width,bottom=x4,color='#F030EA')

    p8 = plt.bar(ind+width2, load1, width,color='blue')
    p9 = plt.bar(ind+width2, store1, width,bottom=load1,color='orange')
    z=np.add(load1,store1)
    p10 = plt.bar(ind+width2, Int1, width,bottom=z,color='green')
    z1=np.add(z,Int1)
    p11 = plt.bar(ind+width2, Float1, width,bottom=z1,color='grey')
    z2=np.add(z1,Float1)
    p12 = plt.bar(ind+width2, Branch1, width,bottom=z2,color='purple')
    z3=np.add(z2,Branch1)
    p13 = plt.bar(ind+width2, Register1, width,bottom=z3,color='#1BCE4B')
    z4=np.add(z3,Register1)
    p14 = plt.bar(ind+width2, Nop1, width,bottom=z4,color='#F030EA')


    # print(list1)
    # print(list2)
    # print(listOthers)

    # plt.ylabel('RATIO')
    plt.title('DIFFERENT TYPE OF INSTRUCTION  COMPARISON NATIVE VS WA FOR '+j)
    plt.xticks(index , (programList1), rotation = 'vertical')
    # plt.yticks(np.arange(0,1.1,.1))
    plt.legend((p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14), ('native-load','native-store','native-int','native-float','native-branch','native-register','native-nop','WA-load','WA-store','WA-int','WA-float','WA-branch','WA-register','WA-nop'))

    plt.show()
