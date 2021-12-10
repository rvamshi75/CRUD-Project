// Ajax Request for insert Data

$("#btnadd").click(function(e){
	e.preventDefault();
	console.log("Submit Button Clicked");

	let name = $("#nameid").val();
	let mail = $("#emailid").val();
	let mobile = $("#mobileid").val();
	let age = $("#ageid").val();
	let gender = $("#gender").val();
	let address = $("#address").val();
	//console.log(name);
	//console.log(mail);
	//console.log(mobile);
	//console.log(age);
	//console.log(gender);
	//console.log(address);

	mydata = {name:name,mail:mail,mobile:mobile,age:age,gender:gender,address:address};
	//console.log(mydata); 
	$.ajax({
		url:"insert.php",
		method : "POST",
		data : JSON.stringify(mydata),
		success: function(data){
			console.log(data);
		}
	})
	
	
});