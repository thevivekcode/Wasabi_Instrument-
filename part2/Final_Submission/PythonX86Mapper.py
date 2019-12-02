import pickle
from pprint import pprint
import json
import gzip
import subprocess
import sys
import threading

def get_end(fun_num, instr_num, filename):
    flag = -1
    dump_file = open(filename)
    dump_lines = dump_file.readlines()
    i = 0
    while i < (len(dump_lines)):
        lines = dump_lines[i]
        if ("func[" + str(fun_num) + "]") in lines:
            i = i + 1
            lines = dump_lines[i]
            while("local[" in lines):
                i = i + 1
                lines = dump_lines[i]
            i = i + instr_num
            lines = dump_lines[i]

            if("if" not in lines):
                print(lines)
                raise Exception('Not if')
            for j in range(len(lines)):
                if(lines[j]=='i' and lines[j+1]=='f'):
                    flag = j
                    break
        elif(flag>-1):
            if("end" in lines or "else" in lines):
                if(lines[flag:flag+3]=='end' or lines[flag:flag+4]=='else'):
                    return int("0x" + str(dump_lines[i+1].split(":")[0].strip()),16)
        i = i + 1

semaphore = threading.Semaphore();
file_name_orig = sys.argv[2]+".html"
file_name=sys.argv[2]
global_stack  = 0
global_memory = 0
memory_allocation = {}
stack_allocation = {}
fp = open(file_name+".objdump.pickle","rb")
data_of_programs = pickle.load(fp)
data_of_programs={int(k):v for k,v in data_of_programs.items()}
fp.close()
temp1 = 0
for key,value in data_of_programs.items():
    stack_allocation[key]={}
    stack_allocation[key]['start'] = temp1
    stack_allocation[key]['end'] = temp1+1024
    stack_allocation[key]['counter'] = temp1
    memory_allocation[key]={}
    memory_allocation[key]['start'] = stack_allocation[key]['end']+1
    memory_allocation[key]['end'] = stack_allocation[key]['end']+1+3071
    memory_allocation[key]['counter'] = stack_allocation[key]['end']+1
    temp1=temp1+4096
#file_name_orig
process = subprocess.Popen(["emrun","--browser","firefox","--port","9997",file_name_orig], stdout=subprocess.PIPE)
tmp = ""
for c in iter(process.stdout.readline, b''):
    data_from_browser = c.decode("utf-8")
    objdump_file = file_name+".objdump.pickle"
    objdump_txt = file_name + ".objdump.txt"
    fp = open(objdump_file,"rb")
    programCounter = pickle.load(fp)
    programCounter={int(k):v for k,v in programCounter.items()}
    fp.close()
    pprint("yooyoyoy")
    data_from_browser = c.decode("utf-8")
    pprint(data_from_browser)
    if "Starting browser" in data_from_browser:
    	continue
    all_data={}
    index=0
    data_from_browser1 = data_from_browser.split("blockend")
    data_from_browser1.pop()

    output_dictionary={}
    instruction_count=0
    output_list=[]

    data_warehouse = {}
    count = 0
    argument_wise_data = {}
    for i in data_from_browser1:
        temp=json.loads(i)
        temp = {int(k):v for k,v in temp.items()}
        for key,value in temp.items():
            data_warehouse[count] = value
            count+=1
    count=0
    for key,value in data_warehouse.items():
        if value['hook_name']=='start' or value['hook_name']=='nop' or value['hook_name']=='unreachable' :
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+value['hook_name']
        elif value['hook_name']== 'if_':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            if value['condition']== False:
                nextval= data_warehouse[key+1]
                pc2=programCounter[nextval['location']['func']]['instructions'][nextval['location']['instr']]
                argument_wise_data[count] = str(int(pc,16))+" 27 "+"if " +str(pc2)
                count+=1
                argument_wise_data[count] = str(int(pc,16))+" 4 "+str(pc2)
            else:
                pc2 = get_end(value['location']['func'],value['location']['instr'],objdump_txt)
                argument_wise_data[count] = str(int(pc,16))+" 27 "+"if " +str(pc2)
                argument_wise_data[count] = str(int(pc,16))+" 5 "+str(pc2)

        elif value['hook_name']== 'br_if':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            if value['condition']== False:
                nextval= data_warehouse[key+1]
                pc2=programCounter[nextval['location']['func']]['instructions'][nextval['location']['instr']]
                argument_wise_data[count] = str(int(pc,16))+" 27 "+"br_if " +str(pc2)
                count+=1
                argument_wise_data[count] = str(int(pc,16))+" 5 "+str(pc2)
            else:
                pc2 = get_end(value['location']['func'],value['location']['instr'],objdump_txt)
                argument_wise_data[count] = str(int(pc,16))+" 27 "+"if " +str(pc2)
                argument_wise_data[count] = str(int(pc,16))+" 4 "+str(pc2)

        elif value['hook_name']== 'br':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count]= str(int(pc,16))+" 27 "+value['hook_name']+ " "+str(value['target']['label'])

        elif value['hook_name']=='local':
            if value['op'] == "local.get":
                addr = stack_allocation[value['location']['func']]['counter']+value['localIndex']
                if(addr<stack_allocation[value['location']['func']]['start']):
                    addr=stack_allocation[value['location']['func']]['start']
                    stack_allocation[value['location']['func']]['counter'] = stack_allocation[value['location']['func']]['start']
                stack_allocation[value['location']['func']]['counter']+=1
            else:
                addr = memory_allocation[value['location']['func']]['counter']+4
                if(addr<memory_allocation[value['location']['func']]['start']):
                    addr=memory_allocation[value['location']['func']]['start']
                    memory_allocation[value['location']['func']]['counter'] = memory_allocation[value['location']['func']]['start']
                memory_allocation[value['location']['func']]['counter']+=4
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+value['op']+ " " +str(addr) + " "+str(value['value'])
        elif value['hook_name']=='global':
            if value['op'] == "global.get":
                addr = stack_allocation[value['location']['func']]['counter']+value['globalIndex']
                if(addr<stack_allocation[value['location']['func']]['start']):
                    addr=stack_allocation[value['location']['func']]['start']
                    stack_allocation[value['location']['func']]['counter'] = stack_allocation[value['location']['func']]['start']
                stack_allocation[value['location']['func']]['counter']+=1
            else:
                addr = memory_allocation[value['location']['func']]['counter']+4
                if(addr<memory_allocation[value['location']['func']]['start']):
                    addr=memory_allocation[value['location']['func']]['start']
                    memory_allocation[value['location']['func']]['counter'] = memory_allocation[value['location']['func']]['start']
                memory_allocation[value['location']['func']]['counter']+=4
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+value['op']+  " " +str(addr) + " "+str(value['value'])
        elif value['hook_name']=='load':
            from_addr = memory_allocation[value['location']['func']]['counter']-4
            to_addr = stack_allocation[value['location']['func']]['counter']
            if(to_addr<stack_allocation[value['location']['func']]['start']):
                to_addr=stack_allocation[value['location']['func']]['start']
                stack_allocation[value['location']['func']]['counter'] = stack_allocation[value['location']['func']]['start']
            if(from_addr<memory_allocation[value['location']['func']]['start']):
                from_addr=memory_allocation[value['location']['func']]['start']
                memory_allocation[value['location']['func']]['counter'] = memory_allocation[value['location']['func']]['start']
            memory_allocation[value['location']['func']]['counter']-=4
            stack_allocation[value['location']['func']]['counter']+=1
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+ value['op'] + " " +str(to_addr)+ " "+str(from_addr)
            count+=1
            argument_wise_data[count] = str(int(pc,16))+" 2 " + str(to_addr)

        elif value['hook_name']=='store':
            to_addr = memory_allocation[value['location']['func']]['counter']
            from_addr = stack_allocation[value['location']['func']]['counter']-1
            if(to_addr<memory_allocation[value['location']['func']]['start']):
                to_addr=memory_allocation[value['location']['func']]['start']
                memory_allocation[value['location']['func']]['counter'] = memory_allocation[value['location']['func']]['start']
            if(from_addr<stack_allocation[value['location']['func']]['start']):
                from_addr=stack_allocation[value['location']['func']]['start']
                stack_allocation[value['location']['func']]['counter'] = stack_allocation[value['location']['func']]['start']
            stack_allocation[value['location']['func']]['counter']-=1
            memory_allocation[value['location']['func']]['counter']+=4
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+ value['op'] + " " +str( value['memarg']['align'] )+ " "+str(value['memarg']['offset'])
            count+=1
            argument_wise_data[count] = str(int(pc,16))+" 3 " + str(to_addr)
        elif value['hook_name']=='binary':
            first = stack_allocation[value['location']['func']]['counter'] -2
            second = stack_allocation[value['location']['func']]['counter'] -1
            if(first<stack_allocation[value['location']['func']]['start']):
                first=stack_allocation[value['location']['func']]['start']
                second = stack_allocation[value['location']['func']]['start']+1
                stack_allocation[value['location']['func']]['counter']=stack_allocation[value['location']['func']]['start']
            else:
                stack_allocation[value['location']['func']]['counter']-=1
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+value['op'] + " " +str( first )+ " " +str(second)
        elif value['hook_name']=='unary':
            addr = stack_allocation[value['location']['func']]['counter'] -1
            if(addr<stack_allocation[value['location']['func']]['start']):
                addr=stack_allocation[value['location']['func']]['start']
                stack_allocation[value['location']['func']]['counter']=stack_allocation[value['location']['func']]['start']

            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] =str(int(pc,16))+" 27 "+ value['op'] + " " +str(addr)
        elif value['hook_name']=='const_':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+value['op'] + " " +str( value['value'] )
        elif value['hook_name']=='return_':
            if value['location']['instr']==-1:
                continue
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+"return"+ " " +str( value['values'])
        elif value['hook_name'] =='end':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+value['hook_name']
        elif value['hook_name']=='call_pre':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count]= str(int(pc,16))+" 27 "+"call"+ " "+str(value['targetFunc'])
        elif value['hook_name']=='select':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            if value['cond'] ==True:
                argument_wise_data[count]= str(int(pc,16))+" 27 "+"i32.const "+str(value['first'])
            else:
                 argument_wise_data[count]= str(int(pc,16))+" 27 "+"i32.const "+str(value['second'])
        elif value['hook_name']=='begin':
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            if value['type']!='if' and value['type']!='function' and value['type']!='block' and value['type']!='loop':
                argument_wise_data[count] = str(int(pc,16))+" 27 "+value['hook_name']
            else:
                argument_wise_data[count] = str(int(pc,16))+" 27 "+"NOP"

        else:
            pc = programCounter[value['location']['func']]['instructions'][value['location']['instr']]
            argument_wise_data[count] = str(int(pc,16))+" 27 "+"NOP"

        count+=1

    data = argument_wise_data
    mpmp=open('mapX86.pickle','rb')
    mapx86=pickle.load(mpmp)
    mpmp.close()
    for key,value in data.items():
        insList= value.split(" ")
        try:
            insList[2] = mapx86[insList[2].strip()]
        except KeyError:
             continue
        data[key]= " ".join(insList)
    out_file_name = file_name+".gz"
    f = gzip.open(out_file_name, 'ab', 9)
    for key,value in data.items():
       f.write((value+"\n").encode())
    f.close()
