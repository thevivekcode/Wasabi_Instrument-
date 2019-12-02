
var count=0;
var block_size = 1000;
var data_to_send={};
// var trace_size_copy = trace_size;
var index_count=0;
var flag = 1
Wasabi.analysisResult = function () {
//console.log(data_to_send);

	if (flag==1)
	{
      var http = new XMLHttpRequest();
      http.onreadystatechange = function() {//Call a function when the state changes.
          if(http.readyState == 4 ) {
              //console.log(http.responseText);
          }
          // else
          //   //console.log("Not found");
      }
      http.open('post', "", false);

      // http.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
      // http.setRequestHeader('content-type','application/json');
			tosend = JSON.stringify(data_to_send) + "blockend"
      http.send(tosend);
      data_to_send={};
      }
}

function data_add(data_list)
{
		// console.log(trace_size)
		console.log("yolo");
    data_to_send[count]=data_list;
    //index_count = (index_count| 0) +1;
    count = (count | 0) +1;
		trace_size--;
		if(trace_size==0)
		{

			Wasabi.analysisResult();
						flag = 0;
					console.log("hi");

		}
}

Wasabi.analysis = {

    start(location) {
        //console.log(location, "start");
        temp = {};
        temp["hook_name"]="start";
        temp["location"]=location;
        // data_add(["start",JSON.stringify(location)]);
        data_add(temp);
        if(count==block_size)
        {
//trace_size--;
          count=0;
          index_count = 0;
          Wasabi.analysisResult();
        }
    },

    nop(location) {
        //console.log(location, "nop");
        temp = {}
        temp["hook_name"]="nop"
        temp["location"]=location
        // data_add(["nop",JSON.stringify(location)]);
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          count=0;
          index_count = 0;
          Wasabi.analysisResult();
        }
    },

    unreachable(location) {
        temp = {}
        temp["hook_name"]="unreachable"
        temp["location"]=location
        //console.log(location, "unreachable");
        // data_add(["unreachable",JSON.stringify(location)]);
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          count=0;
          index_count = 0;
          Wasabi.analysisResult();
        }

    },

    if_(location, condition) {
        //console.log(location, "if, condition =", condition);
        temp = {}
        temp["hook_name"]="if_"
        temp["location"]=location
        // data_add(["if_",JSON.stringify(location),JSON.stringify(condition)]);
        temp["condition"]=condition
        data_add(temp)
        count--;
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          count=0;
          index_count = 0;
          Wasabi.analysisResult();
        }

    },

    br(location, target) {
        //console.log(location, "br, to label", target.label, "(==", target.location, ")");
        temp = {}
        temp["hook_name"]="br"
        temp["location"]=location
        temp["target"] = target
        // data_add(["br",JSON.stringify(location),JSON.stringify(target)]);
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    br_if(location, conditionalTarget, condition) {
        //console.log(location, "br_if, (conditionally) to label", conditionalTarget.label, "(==", JSON.stringify(conditionalTarget.location,null,2), "), condition =", condition);
        // data_add(["br_if",JSON.stringify(location),JSON.stringify(conditionalTarget),JSON.stringify(condition)]);
        temp = {}
        temp["hook_name"]="br_if"
        temp["location"]=location
        temp["conditionalTarget"] = conditionalTarget
        temp["condition"] = condition
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    br_table(location, table, defaultTarget, tableIdx) {
        //console.log(location, "br_table, table =", table, ", default target =", defaultTarget, ", table index =", tableIdx);
        // data_add(["br_table",JSON.stringify(location),JSON.stringify(table),JSON.stringify(defaultTarget),JSON.stringify(tableIdx)]);
        temp = {}
        temp["hook_name"]="br_table"
        temp["location"]=location
        temp["table"]=table
        temp["defaultTarget"] = defaultTarget
        temp["tableIdx"] = tableIdx
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    begin(location, type) {
        //console.log(location, "begin", type);
        // data_add(["begin",JSON.stringify(location),JSON.stringify(type)]);
        temp = {}
        temp["hook_name"]="begin"
        temp["location"]=location
        temp["type"]=type
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    // ifLocation === location of the matching if block for else
    end(location, type, beginLocation, ifLocation) {
        //console.log(location, "end", type, "(begin @", beginLocation, ", if begin @", ifLocation, ")");
        // data_add(["end",JSON.stringify(location),JSON.stringify(type),JSON.stringify(beginLocation),JSON.stringify(ifLocation)]);
        temp = {}
        temp["hook_name"]="end"
        temp["location"]=location
        temp["beginLocation"]=beginLocation
        temp["ifLocation"]=ifLocation
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    drop(location, value) {
        //console.log(location, "drop, value =", value);
        // data_add(["drop",JSON.stringify(location),JSON.stringify(value)]);
        temp = {}
        temp["hook_name"]="drop"
        temp["location"]=location
        temp["value"]=value
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    select(location, cond, first, second) {
        //console.log(location, "select, condition =", cond, "first =", first, "second =", second);
        // data_add(["select",JSON.stringify(location),JSON.stringify(cond),JSON.stringify(first),JSON.stringify(second)]);
        temp={}
        temp["hook_name"]="select"
        temp["location"]=location
        temp["cond"]=cond
        temp["first"]=first
        temp["second"]=second
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    // indirectTableIdx === undefined iff direct call, for indirect calls it is a number
    call_pre(location, targetFunc, args, indirectTableIdx) {
        //console.log(location, (indirectTableIdx === undefined ? "direct" : "indirect"), "call", "to func #", targetFunc, "args =", args);
        // data_add(["call_pre",JSON.stringify(location),JSON.stringify(targetFunc),JSON.stringify(args),JSON.stringify(indirectTableIdx)]);
        temp = {}
        temp["hook_name"]="call_pre"
        temp["location"]=location
        temp["targetFunc"] = targetFunc
        temp["args"]=args
        temp["indirectTableIdx"]=indirectTableIdx
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    call_post(location, values) {
        temp = {}
        temp["hook_name"]="call_post"
        temp["location"]=location
        temp["values"]=values
        data_add(temp)
        //console.log(location, "call result =", values);
        // data_add(["call_post",JSON.stringify(location),JSON.stringify(values)]);
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    return_(location, values) {
        //console.log(location, (location.instr === -1) ? "implicit" : "explicit", "return, values = ", values);
        // data_add(["return_",JSON.stringify(location),JSON.stringify(values)]);
        temp = {}
        temp["hook_name"]="return_"
        temp["location"]=location
        temp["values"]=values
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    const_(location, op, value) {
        //console.log(location, op, "value =", value);
        // data_add(["const_",JSON.stringify(location),JSON.stringify(op),JSON.stringify(value)]);
        temp = {}
        temp["hook_name"]="const_"
        temp["location"]=location
        temp["op"]=op
        temp["value"]=value
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    unary(location, op, input, result) {
        //console.log(location, op, "input =", input, "result =", result);
        // data_add(["unary",JSON.stringify(location),JSON.stringify(op),JSON.stringify(input),JSON.stringify(result)]);
        temp = {}
        temp["hook_name"]="unary"
        temp["location"]=location
        temp["op"]=op
        temp["input"]=input
        temp["result"]=result
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          count=0;
          index_count = 0;
          Wasabi.analysisResult();
        }

    },

    binary(location, op, first, second, result) {
        //console.log(location, op, "first =", first, " second =", second, "result =", result);
        // data_add(["binary",JSON.stringify(location),JSON.stringify(op),JSON.stringify(first),JSON.stringify(second),JSON.stringify(result)]);
        temp = {}
        temp["hook_name"]="binary"
        temp["location"]=location
        temp["op"]=op
        temp["first"]=first
        temp["second"]=second
        temp["result"]=result
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    load(location, op, memarg, value) {
        //console.log(location, op, "value =", value, "from =", memarg);
        // data_add(["load",JSON.stringify(location),JSON.stringify(op),JSON.stringify(memarg),JSON.stringify(value)]);
        temp = {}
        temp["hook_name"]="load"
        temp["location"]=location
        temp["op"]=op
        temp["memarg"]=memarg
        temp["value"]=value
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    store(location, op, memarg, value) {
        //console.log(location, op, "value =", value, "to =", memarg);
        // data_add(["store",JSON.stringify(location),JSON.stringify(op),JSON.stringify(memarg),JSON.stringify(value)]);
        temp = {}
        temp["hook_name"]="store"
        temp["location"]=location
        temp["op"]=op
        temp["memarg"]=memarg
        temp["value"]=value
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    memory_size(location, currentSizePages) {
        //console.log(location, "memory_size, size (in pages) =", currentSizePages);
        // data_add(["memory_size",JSON.stringify(location),JSON.stringify(currentSizePages)]);
        temp = {}
        temp["hook_name"]="memory_size"
        temp["location"]=location
        temp["currentSizePages"]=currentSizePages
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    memory_grow(location, byPages, previousSizePages) {
        //console.log(location, "memory_grow, delta (in pages) =", byPages, "previous size (in pages) =", previousSizePages);
        // data_add(["memory_grow",JSON.stringify(location),JSON.stringify(byPages),JSON.stringify(previousSizePages)]);
        temp = {}
        temp["hook_name"]="memory_grow"
        temp["location"]=location
        temp["byPages"]=byPages
        temp["previousSizePages"]=previousSizePages
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    local(location, op, localIndex, value) {
        //console.log(location, op, "local #", localIndex, "value =", value);
        // data_add(["local",JSON.stringify(location),JSON.stringify(op),JSON.stringify(localIndex),JSON.stringify(value)]);
        temp = {}
        temp["hook_name"]="local"
        temp["location"]=location
        temp["op"]=op
        temp["localIndex"]=localIndex
        temp["value"]=value
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },

    global(location, op, globalIndex, value) {
        //console.log(location, op, "global #", globalIndex, "value =", value);
        // data_add(["global",JSON.stringify(location),JSON.stringify(op),JSON.stringify(globalIndex),JSON.stringify(value)]);
        temp = {}
        temp["hook_name"]="global"
        temp["location"]=location
        temp["op"]=op
        temp["globalIndex"]=globalIndex
        temp["value"]=value
        data_add(temp)
        //if(trace_size_copy==0)
          //return true
        if(count==block_size)
        {
//trace_size--;
          index_count = 0;
          count=0;
          Wasabi.analysisResult();
        }

    },
};
