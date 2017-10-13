$("#text").hover(function(){
  $("#text_back").show();
  $("#pic_back").hide();
  $("#link_back").hide();    
});

$("#pic").hover(function(){
  $("#text_back").hide();
  $("#pic_back").show();
  $("#link_back").hide();      
});

$("#link").hover(function(){
  $("#text_back").hide();
  $("#pic_back").hide();
  $("#link_back").show();       
});

$(document).ready(function(){ 
  $("#text_back").show();
  $("#pic_back").hide();
  $("#link_back").hide();         
}); 