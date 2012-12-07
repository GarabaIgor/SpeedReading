	$(function()
	{
		var nextInd = 1;
		var cur = 0;
		var sec = 0;
		var min = 0;
		$('td').live('click',function()
			{
				
				//console.log($(this).text() + " " + nextInd );
				var $this = $(this);
				if(nextInd == parseInt($this.text()))
				{
					$this.css('background','#00D500');
					nextInd++;
					cur++;
					console.log(nextInd + " " + $this.text());
					
					
				}
				else 
				{
					$this.css('background','red');
				}
				setTimeout(
					function()
					{
					
						
						$this.css('background','white');
					},250);
				//nextInd == 26 && cur == 25
				if(nextInd == 2)
				{
				clearInterval(timerId);
				// $.ajax(
				// 	{
				// 		url: "http://127.0.0.1:8000/get_schulte_table_inf/",
    //   				    type: "POST",
    //    				    data: {"ex_name":"SchulteTable","min":min,"sec":sec},
    //     				dataType:"json",

				// 	});
				template = $.trim($("#resultTime").html());
				var temp = template.replace(/{minResult}/ig,min)
								   .replace(/{secResult}/ig,sec);
				
				$("#resultTime").replaceWith(temp); 
				$("#myModal").modal("show");
					
				
			}
				
			});
		timerId = setInterval(function() { 
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
		//Отправляю по кнопке завершить упражнение
		$("#finish_ex").on("click",function(){

				$.ajax(
					{
						url: "http://127.0.0.1:8000/get_schulte_table_inf/",
      				    type: "POST",
       				    data: {"ex_name":"SchulteTable","min":min,"sec":sec},
        				dataType:"json",

					});
				// template = $.trim($("#resultTime").html());
				// var temp = template.replace(/{minResult}/ig,min)
				// 				   .replace(/{secResult}/ig,sec);
				
				// $("#resultTime").replaceWith(temp); 
		});
		
	});


