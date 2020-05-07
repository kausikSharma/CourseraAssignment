(function(global){

var ajaxUtils={};

//Returns an XMLHttp response object using Ajax
function getRequestObject()
{
	if(window.XMLHttpRequest)//if window support this AJAX call
	{
		return(new XMLHttpRequest());//send the AJAX call object
	}

	else if (window.ActiveXObject)//(optional) For very old IE browser
	{
		return(new ActiveXObject("Microsoft.XMLHTTP"));
	}
	else{
		global.alert("Ajax is not supported !!");
		return(null);
	}
}

//Makes handleResponse which tasks are to check 'readyState' and 'status' and fetch the code from the server
//and call and send the fetched data responseHandler function to 'script.js'
function handleResponse(request,responseHandler,isJasonResponse)
{
	if((request.readyState==4) && (request.status==200))
	{
		if(isJasonResponse==undefined)
		{
			isJasonResponse=true;
		}
		if(isJasonResponse)//Fetched info is in Jason format and we need to convert it into object
		{
			responseHandler(JSON.parse(request.responseText));
		}
		else{//if fetched data is not in JSON format then just smply send it up
			responseHandler(request.responseText);
		}
	}
}


//Makes an AJAX sendGetRequest propertise to handle further AJAX request

ajaxUtils.sendGetRequest=function(requestUrl,responseHandler,isJasonResponse)
{
	var request=getRequestObject();
	request.onreadystatechange=function()
	{
		handleResponse(request,responseHandler,isJasonResponse);
	}
	request.open("GET",requestUrl,true);
	request.send(null);

}


//Expose utility to the global object
global.$ajaxUtils=ajaxUtils;

})(window);