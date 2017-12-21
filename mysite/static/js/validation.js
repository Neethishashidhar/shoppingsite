
function disable_dropdowns(){
	document.getElementById("id_branch").disabled = true;
	document.getElementById("id_customer").disabled = true;
	$("#id_table tr:last").hide();
	$('#id_table tr:last').prev('tr').hide()
}


function clearBranch(){
	$("#id_branch option:gt(0)").remove();
	  }

function resetValues(){
	if(document.getElementById("id_organisation").value === ""){
		document.getElementById("id_branch").value=0;
		document.getElementById("id_customer").value=0;
	};
	
}
function loadbranch(){
	resetValues();
	clearBranch();
	document.getElementById("id_branch").disabled = false;
	var org = document.getElementById("id_organisation").value;
	var br_ob = document.getElementById("id_br").options;
	var br_len = document.getElementById("id_br").length;
	var sel = document.getElementById("id_branch");
	for(var i = 1; i < br_len; i++) {
		var br_val = br_ob[i].value;
		eval('var obj='+ br_val);
		for (var key in obj) {
			    if (obj.hasOwnProperty(key)) {
			    	if(key == "organisation_id"){
			    		if(obj[key] == org ){
			    			var el = document.createElement("option");
			    		    el.textContent = obj["name"];
			    		    el.value = obj["id"];
			    		    sel.appendChild(el);
			     }
			  }
		   }
		}
	}
}

function clearCustomer(){
		$("#id_customer option:gt(0)").remove();
}


function loadcustomer(){
	clearCustomer();
	document.getElementById("id_customer").disabled = false;
	var branch = document.getElementById("id_branch").value;
	var cust_ob = document.getElementById("id_cust").options;
	var cust_len = document.getElementById("id_cust").length;
	var sel = document.getElementById("id_customer");
	for(var i = 1; i < cust_len; i++) {
		var cust_val = cust_ob[i].value;
		eval('var obj='+ cust_val);
		for (var key in obj) {
			    if (obj.hasOwnProperty(key)) {
			    	if(key == "branch_id"){
			    		if(obj[key] == branch ){
			    			var el = document.createElement("option");
			    		    el.textContent = obj["name"];
			    		    el.value = obj["id"];
			    		    sel.appendChild(el);
			     }
			  }
		   }
		}
	}
}




