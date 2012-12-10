$(function() {
	$("#get_content").on("click",function()
	{
		text_name = $("#texts_names option:selected").val();
		$.get("http://127.0.0.1:8000/vertical_html/",{"text_name":text_name},function(html){
  		   // $("head").append("<link href=\"/static/Vertical.css\" rel=\"stylesheet\">");
  		   $(".navbar").after("<div class=\"top_left_corner\"><a id=\"restart\" class=\"btn btn-info\"><i class=\"icon-refresh\" ></i> Начать заново</a><p class=\"timer\"><span id=\"min\">0</span>:<span id=\"sec\">0</span></p></div>");

  		   $("#content_container").html(html);

  		$('body').on("click","#finish_reading",function(){
  			// $(".navbar").after("<div class=\"top_left_corner\"><a id=\"restart\" class=\"btn btn-info\"><i class=\"icon-refresh\" ></i> Начать заново</a><p class=\"timer\"><span id=\"min\">0</span>:<span id=\"sec\">0</span></p></div>");
  			$.get("http://127.0.0.1:8000/vertical_questionare_html/",{"text_name":text_name},function(html){
  					// $.getScript("/static/vertical_questionare.js");
  					$(".top_left_corner").remove();
  		   			$("#content_container").html(html);
  		   		});
  		});

  		$("body").on("click","#check_result",function(){
  		serialized_arr = $("form").serializeArray();
  		// var ob = {"text_name":text_name};
  		// serialized_arr.push(ob);

		console.log(serialized_arr);

		$.ajax(
					{
						url: "http://127.0.0.1:8000/vertical_questionare_result/",
      				    type: "POST",
       				    data: serialized_arr,
        				dataType:"json",

					});
		

	
	});
	});
	});
});