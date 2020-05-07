function sayHello()
{
	var name=document.getElementById("content").value;
	//console.log(name);

	var msg="<h1>This is "+name+"</h1>"

	document.getElementById("write").innerHTML=msg;

	var title=document.getElementById("title").textContent
	title+=" "+name;

	document.getElementById("title").textContent=title;
}