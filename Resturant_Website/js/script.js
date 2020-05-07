//Here we use Jquery because collapsabe-nav functionality is based on jquery
//Target: anywhere we touched, collapsable nav loose its focus
$(function(){//Same as document.addEventLister("DOMContentLoaded".....)

	//same as document.querySelector("#navbarToggle")

	$("#navbarToggle").blur(function(event){

		var screenwidth=window.innerWidth;
		if(screenwidth<768){
			$("#collapsable-nav").collapse('hide');
		}
	});


});



(function(global){
	var dc={};
	var homeHtml="snippet/home-snippet.html";

	//fuction for inserting innerHTML for  'select'
	var insertHtml=function(selector,html){
		var targetElement=document.querySelector(selector);
		targetElement.innerHTML=html;
	};
	//show loading icon inside element identified by 'selector'
	var showLoading=function(selector){
		var html="<div class='text-center'>";
		html+="<img src='image/Wedges-3s-200px.gif'></div>";
		insertHtml(selector,html);
	};

	//On Page Load(Before images or css)
	document.addEventListener("DOMContentLoaded",function(event){

		showLoading('#main-content');
		$ajaxUtils.sendGetRequest(
			homeHtml,
			function (responseText){
				document.querySelector("#main-content")
				.innerHTML=responseText;
			},
			false);
		
	});

	global.$dc=dc;

})(window);