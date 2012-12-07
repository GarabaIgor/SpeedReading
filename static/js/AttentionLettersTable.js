 $(function()
	{

 $(document).bind("contextmenu",function(e){
              return false;
       }); 
		$('td').mousedown(function(event) {
    switch (event.which) {
        case 1:
        	if(!$(this).attr("id"))
            $(this).attr("id","selected");
            break;
        case 2:
            // alert('Middle mouse button pressed');
            break;
        case 3:
        	if(!$(this).attr("id"))
            $(this).attr("id","selected2");
            break;
        default:
            alert('You have a strange mouse');
    }
});
	$("#check_table_b").on("click",function(){
        var selected = $("#selected").text();
        $("#letters_table td").each(function() {
        var td = $(this);
        // TODO принять значение букв через AJAX
        if(td.attr("id") == "selected" && td.text() != "К")
        {
            td.attr("id","selected_mistake");
            console.log(td.attr("id"));
        }
        if(td.attr("id") == "selected2" && td.text() != "Н")
        {
            td.attr("id","selected_mistake");
            console.log(td.attr("id"));
        }
        if(!td.attr("id") && (td.text() == "К" || td.text() == "Н"))
        {
            td.attr("id","selected_mistake");
            console.log(td.attr("id"));
        }

        

    // compare id to what you want
});
    });
		
 	});

