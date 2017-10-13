//query.js
//

$(document).ready(function(){ 
  var height=$("#show_text").height();
	if(height<200){
		$("#show_text").css('height',200);
	}else{
		$("#show_text").css('height','auto');
	}

}); 