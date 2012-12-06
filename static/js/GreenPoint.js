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
				alert('Упражнение окончено');
				clearInterval(timerId);
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
