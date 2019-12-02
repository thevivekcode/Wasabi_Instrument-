{
    const counts = {};
    const final_out = {};
    var stack = [];
    var count=0;
    const func_counts={};
    const func_instr_counts = {};


    Wasabi.analysisResult = function () {
        const keysSorted = Object.keys(counts).sort(function(a,b){return counts[b]-counts[a]});
        //document.getElementById("output").value+="---------------------------------- \n";
        var temp="";

        //document.getElementById("output").value = JSON.stringify(counts,null,2);
        document.getElementById("output").value+=JSON.stringify(func_instr_counts,null,2);

        //console.log(temp);
        var http = new XMLHttpRequest();
        http.onreadystatechange = function() {//Call a function when the state changes.
            if(http.readyState == 4) {
                //console.log(http.responseText);
            }
        }
        counts["total_count"]=count;

        http.open('post', "", true);

        //Send the proper header information along with the request

    	final_out["exp2and3"] = JSON.stringify(counts,null,2);
    	final_out["exp4"] = JSON.stringify(func_counts,null,2);
      final_out["exp4new"] = JSON.stringify(func_instr_counts,null,2);
      http.send(JSON.stringify(final_out,null,2));

    };



    function incInstr(instr)
    {

        counts[instr] = (counts[instr] | 0) + 1;
        count++;

    }

    function total_counts()
    {
    	count++;
    }

    function hot_code(func)
    {
    	func_counts[func.toString()]=(func_counts[func.toString()]|0)+1;
    }

    function count_func_instr_counts(fun)
    {
      func_instr_counts[fun] = (func_instr_counts[fun] | 0)+1;
    }

    function find_top()
    {
      var x = stack.pop();
      stack.push(x);
      return x;
    }
    function fctName(fctId)
    {
          const fct = Wasabi.module.info.functions[fctId];
          if (fct.export[0] !== undefined) return fct.export[0];
          if (fct.import !== null) return fct.import;
          return fctId;
  }
    Wasabi.analysis = {
    //
        // hooks that directly correspond to one instruction
        nop(loc) { incInstr("nop");count_func_instr_counts(find_top());  },
        unreachable(loc) { total_counts(); count_func_instr_counts(find_top()); },
        if_(loc, cond) { total_counts(); count_func_instr_counts(find_top()); },
        br(loc, target) { incInstr("branch"); count_func_instr_counts(find_top()); },
        br_if(loc, target, cond) { incInstr("branch");count_func_instr_counts(find_top());  },
        br_table(loc, table, def, idx) { incInstr("branch");count_func_instr_counts(find_top());  },
        drop(loc, val) { total_counts();count_func_instr_counts(find_top()); },//incInstr("drop") },
        select(loc, fst, snd, cond) { total_counts();count_func_instr_counts(find_top()); },//incInstr("select") },
        memory_size(loc, val) { total_counts();count_func_instr_counts(find_top()); },//incInstr("memory_size") },
        memory_grow(loc, delta, old) { incInstr("register");count_func_instr_counts(find_top());  },

        // hooks that correspond to multiple instructions -> use op argument
        unary(loc, op, input, result) {
        					if(op.includes("const"))
        						incInstr("register");
        					else if(op.includes("i32") || op.includes("i64"))
        						incInstr("integer");
        					else if(op.includes("f32") || op.includes("f64"))
        						incInstr("float");
                  count_func_instr_counts(find_top());
        			      },
        binary(loc, op, first, second, result) {
							if(op.includes("const"))
        							incInstr("register");
							else if(op.includes("i32") || op.includes("i64"))
								incInstr("integer");
							else if(op.includes("f32") || op.includes("f64"))
								incInstr("float");
              count_func_instr_counts(find_top());
        					},
        load(loc, op, memarg, val) { incInstr("load");count_func_instr_counts(find_top());  },
        store(loc, op, memarg, val) { incInstr("store");count_func_instr_counts(find_top());  },
        local(loc, op, idx, val) { incInstr("register");count_func_instr_counts(find_top());  },
        global(loc, op, idx, val) { incInstr("register");count_func_instr_counts(find_top());  },

        // special casesconsole.log(location, "start");

        call_pre(location, targetFunc, args, indirectTableIdx)
        {
          const caller = fctName(location.func);
          const callee = fctName(targetFunc);
          total_counts();
          count_func_instr_counts(find_top());
          stack.push(callee);
          hot_code(callee);
          if (count_func_instr_counts[callee]==null)
            count_func_instr_counts[callee]=0;


        },

        const_(loc, op, val) {
            total_counts();
            count_func_instr_counts(find_top());
        },
        begin({func, instr}, type) {
            // if is already counted by if_ hook, function begin is implicit


            if (type !== "if" && type !== "function")
            {

            	total_counts();

              count_func_instr_counts(find_top());
            }
        },
        return_({func, instr}, vals) {
            // do not count implicit returns
            if (instr >= 0)
            {
            	total_counts();
              count_func_instr_counts(find_top());
            	//console.log("------------------------------");
            	//console.log(Wasabi.analysisResult());
              if(func==find_top())
                stack.pop();



            }
        },
        start(location) {
    		total_counts();

        count_func_instr_counts(find_top());
    	},
    	end(location, type, beginLocation, ifLocation) {
    		total_counts();
        if(type=="function")
          Wasabi.analysisResult();
          count_func_instr_counts(find_top());

    	},
    	call_post(location, values){
    		total_counts();
        count_func_instr_counts(find_top());
        stack.pop();
    	},

        // not hooked: end (not really executed anyway), start (no real instruction), call_post (already counted)
    };

}
