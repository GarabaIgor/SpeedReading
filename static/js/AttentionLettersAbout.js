jQuery(document).ready(function() {
	var chosen_letters = "";
  $("#sendLetters").on('click',function()
  {
    chosen_letters = $("#list option:selected").val();
    console.log(chosen_letters.length);
  $.post("http://127.0.0.1:8000/attention_letters/",{"chosen_letters":chosen_letters},function(html){
  		   $("head").append("<link href=\"/static/AttentionLettersTable.css\" rel=\"stylesheet\">");
  		   $("head").append("<script type=\"text/javascript\" src=\"/static/AttentionLettersTable.js\"></script>");
  		 
  		
  		
  		 // $.getScript("/static/AttentionLettersTable.js",function()
  		 // {
  		 // 	// alert("&777");
  		 // });


  		$("#exercise_zone").html(html);
  		
  },'html');
          
   
}); 

// Если одна буква

$('body').on("mousedown","td",function(event) {
	if(chosen_letters.length == 1)
	{
		if (event.which == 1) {
       	 	
	        	if(!$(this).attr("id"))
	            $(this).attr("id","selected");
	            
	}
	}
	if(chosen_letters.length == 2)
	{
		if (event.which == 1) {
       	 	
	        	if(!$(this).attr("id"))
	            $(this).attr("id","selected");
	            
	}
		if(event.which == 3)
		{
        	if(!$(this).attr("id"))
            $(this).attr("id","selected2");
    	}
            
	}
          
        
     
});

$("body").on("click","#check_table_b",function(){
        var selected = $("#selected").text();
        $("#letters_table td").each(function() {
        var td = $(this);
        // TODO принять значение букв через AJAX
        if(td.attr("id") == "selected" && td.text() != chosen_letters[0])
        {
            td.attr("id","selected_mistake");
            // console.log(td.attr("id"));
        }
        if(td.attr("id") == "selected2" && td.text() != chosen_letters[1])
        {
            td.attr("id","selected_mistake");
            // console.log(td.attr("id"));
        }
        if(!td.attr("id") && (td.text() == chosen_letters[0] || td.text() == chosen_letters[1]))
        {
            td.attr("id","selected_mistake");
            // console.log(td.attr("id"));
        }

        

    // compare id to what you want
});
    });

});
