jQuery(document).ready(function() {
	var h = $("#green_point_text").height();
	var w = $("#green_point_text").width();
	var sec = 0;
	var min = 0;
	console.log(h)
	$("#circle").css("margin-left",w/2);
	$("#circle").css("margin-top",h/2+10);
	timerId = setInterval(function() { 
			if(min==10)
			{
				// alert('Упражнение окончено');

				$.ajax(
					{
						url: "http://127.0.0.1:8000/get_green_point/",
      				    type: "POST",
       				    data: {"ex_name":"GreenPoint","done":"true"},
        				dataType:"json",

					});
				
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
});
