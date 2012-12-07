$(function() {
	$("#double_images_start").on("click",function(){
		$.getJSON("http://127.0.0.1:8000/double_images_json/",{},function(json){
  		   // $("head").append("<link href=\"/static/AttentionLettersTable.css\" rel=\"stylesheet\">");
  		   // $("head").append("<script type=\"text/javascript\" src=\"/static/AttentionLettersTable.js\"></script>");
  		 
        $("#content_container").html(json.html_content);
        $("#content_container").css({"text-align":"center","padding-top":"2em"});
        $(".navbar").after("<div class=\"top_left_corner\"><a class=\"btn btn-info\"><i class=\"icon-refresh\" ></i> Начать заново</a><p class=\"timer\"><span id=\"min\">0</span>:<span id=\"sec\">0</span></p></div>");
  		
  		var sec = 0;
	var min = 0;
	timerId = setInterval(function() { 
			if(sec==5)
			{
				
				clearInterval(timerId);
				alert('Упражнение окончено');
			}
			if(sec != 60) 
			{
				$("#sec").text(++sec);
			}
			else if(sec == 60)
			{
				sec = 0;
				$("#sec").text(sec);
				$("#min").text(++min);
			}
			},1000);
  		
  },'json');
	})

	
});