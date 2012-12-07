jQuery(document).ready(function() {
	var chosen_letters = "";
  var letter1_count = 0;
  var letter2_count = 0;
  // var letter3_count = 0;
  var mistake_count = 0;
  var not_found_count = 0;
  var letter1_count_orig = 0;
  var letter2_count_orig = 0;
  // var letter3_count_orig = 0;
  $("#sendLetters").on('click',function()
  {
    chosen_letters = $("#list option:selected").val();
    console.log(chosen_letters.length);
  $.getJSON("http://127.0.0.1:8000/attention_letters_json/",{"chosen_letters":chosen_letters},function(json){
  		   $("head").append("<link href=\"/static/AttentionLettersTable.css\" rel=\"stylesheet\">");
  		   $("head").append("<script type=\"text/javascript\" src=\"/static/AttentionLettersTable.js\"></script>");
  		 
        // console.log(html);
        // console.log(typeof(html));
        
         // console.log(json.letter1_count);
  		
  		
  		 // $.getScript("/static/AttentionLettersTable.js",function()
  		 // {
  		 // 	// alert("&777");
  		 // });
       letter1_count_orig = json.letter1_count;
       letter2_count_orig = json.letter2_count;

  		$("#exercise_zone").html(json.html_content);
  		
  },'json');
          
   
}); 

// Если одна буква

$('body').on("mousedown","td",function(event) {
	if(chosen_letters.length == 1)
	{
		if (event.which == 1) {
       	 	
	        	if(!$(this).attr("id"))
            {
	            $(this).attr("id","selected");
            letter1_count++;
          }
	            
	}
	}
	if(chosen_letters.length == 2)
	{
		if (event.which == 1) {
       	 	
	        	if(!$(this).attr("id"))
            {
	            $(this).attr("id","selected");
            letter1_count++;
          }
	            
	}
		if(event.which == 3)
		{
        	if(!$(this).attr("id"))
          {
            $(this).attr("id","selected2");
          letter2_count++;
        }
    	}
            
	}
          
        
     
});

$("body").on("click","#check_table_b",function(){
        $('body').unbind('mousedown');
        var selected = $("#selected").text();
        $("#letters_table td").each(function() {
        var td = $(this);
        // TODO принять значение букв через AJAX
        if(td.attr("id") == "selected" && td.text() != chosen_letters[0])
        {
            td.attr("id","selected_mistake");

            letter1_count--;
            mistake_count++;
            // console.log(td.attr("id"));
        }
        if(td.attr("id") == "selected2" && td.text() != chosen_letters[1])
        {
            td.attr("id","selected_mistake");

            letter2_count--;
            mistake_count++;
            // console.log(td.attr("id"));
        }
        if(!td.attr("id") && (td.text() == chosen_letters[0] || td.text() == chosen_letters[1]))
        {
            td.attr("id","selected_mistake");
            mistake_count++;
            // not_found_count++;
            // console.log(td.attr("id"));
        }



        

    // compare id to what you want
});
        template = $.trim($("#resultInf").html());
        var temp = template.replace(/{letter1_count}/ig,letter1_count)
                   .replace(/{letter2_count}/ig,letter2_count)
                   .replace(/{letter1_count_orig}/ig,letter1_count_orig)
                   .replace(/{letter2_count_orig}/ig,letter2_count_orig)
                   .replace(/{mistake_count}/ig,mistake_count)
                   .replace(/{not_found_count}/ig,not_found_count);
        $("#resultInf").replaceWith(temp); 
        console.log(temp);
        $("#myModal").modal("show");
    });

$("body").on("click","#finish_ex",function(){
  
  $.ajax(
          {
            url: "http://127.0.0.1:8000/get_attention_letters_result/",
                  type: "POST",
                  data: {"ex_name":"AttentionLetters","mistake_count":mistake_count},
                dataType:"json",

          });
});
});
