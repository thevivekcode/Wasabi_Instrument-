/*
 * Copyright 2002-2019 Intel Corporation.
 * 
 * This software is provided to you as Sample Source Code as defined in the accompanying
 * End User License Agreement for the Intel(R) Software Development Products ("Agreement")
 * section 1.L.
 * 
 * This software and the related documents are provided as is, with no express or implied
 * warranties, other than those that are expressly stated in the License.
 */

#include <iostream>
#include <fstream>
#include "pin.H"
using std::cerr;
using std::ofstream;
using std::ios;
using std::string;
using std::endl;

ofstream OutFile;

// The running count of instructions is kept here
// make it static to help the compiler optimize docount
static UINT64 icount,branchcount,regcount,floatcount,nopcount ,loadcount, storecount, intcount= 0;

// This function is called before every instruction is executed
VOID docount() { icount++; }
VOID dobranchcount() { branchcount++; }
VOID domovcount() { regcount++; }
VOID dofloatcount() { floatcount++; }
VOID donopcount() { nopcount++; }
VOID doloadcount() {loadcount++;}
VOID dostorecount() {storecount++;}
VOID dointcount() {intcount++;}
    
// Pin calls this function every time a new instruction is encountered
VOID Instruction(INS ins, VOID *v)
{
    // Insert a call to docount before every instruction, no arguments are passed
	//INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)docount, IARG_END);

	//Dynamic Ins Count
	INS_InsertPredicatedCall(ins, IPOINT_BEFORE, (AFUNPTR)docount, IARG_END);

    	if(INS_IsBranch(ins))
    		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)dobranchcount, IARG_END);

	else if(INS_IsMov(ins) && INS_OperandIsReg(ins,0) && (INS_OperandIsReg(ins,1) || INS_OperandIsImmediate(ins,1)))
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)domovcount, IARG_END);
	
	else if(INS_Category(ins)== XED_CATEGORY_X87_ALU)
	INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)dofloatcount, IARG_END);
	
	else if(INS_Category(ins)== XED_CATEGORY_BINARY || INS_Category(ins)== XED_CATEGORY_LOGICAL)
	INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)dointcount, IARG_END);
	

	else if(INS_IsNop(ins) )
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)donopcount, IARG_END);

	else if(INS_MemoryOperandIsRead(ins ,0) )
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)doloadcount, IARG_END);

	else if(INS_MemoryOperandIsWritten(ins,0))
		INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)dostorecount, IARG_END);
}

KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE, "pintool",
    "o", "inscount.out", "specify output file name");

// This function is called when the application exits
VOID Fini(INT32 code, VOID *v)
{
    // Write to a file since cout and cerr maybe closed by the application
	OutFile.setf(ios::showbase);
	OutFile << "DynamicCount " << icount << endl;
	//OutFile  << icount << endl;
	OutFile << "LoadCount " << loadcount << endl;
	//OutFile  << loadcount << endl;
	OutFile << "StoreCOunt " << storecount << endl;
	//OutFile  << storecount << endl;
	OutFile << "Int " << intcount << endl;
	//OutFile << countint << endl;
	OutFile << "Float " << floatcount << endl;
	//OutFile << countfloat << endl;
	OutFile << "Branchcount " << branchcount << endl;
	//OutFile << branchcount << endl;
	OutFile << "RegsiterCount " << regcount << endl;
	//OutFile << regcount << endl;
	OutFile << "NOPcount " << nopcount << endl;
	//OutFile  << nopcount << endl;
	
	

	

    OutFile.close();
}

/* ===================================================================== */
/* Print Help Message                                                    */
/* ===================================================================== */

INT32 Usage()
{
    cerr << "This tool counts the number of dynamic instructions executed" << endl;
    cerr << endl << KNOB_BASE::StringKnobSummary() << endl;
    return -1;
}

/* ===================================================================== */
/* Main                                                                  */
/* ===================================================================== */
/*   argc, argv are the entire command line: pin -t <toolname> -- ...    */
/* ===================================================================== */

int main(int argc, char * argv[])
{
    // Initialize pin
    if (PIN_Init(argc, argv)) return Usage();

    OutFile.open(KnobOutputFile.Value().c_str());

    // Register Instruction to be called to instrument instructions
    INS_AddInstrumentFunction(Instruction, 0);

    // Register Fini to be called when the application exits
    PIN_AddFiniFunction(Fini, 0);
    
    // Start the program, never returns
    PIN_StartProgram();
    
    return 0;
}
