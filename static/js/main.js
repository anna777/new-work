console.log("fgfgfg")
alert( "As you can see, the link no longer took you to jquery.com" );

$(document).ready(function () {
  console.log("fgfgfg")
  alert( "As you can see, the link no longer took you to jquery.com" );
  size_li = $("#loade").size();
  x=3;
  $('#loade ('+x+')').show();
  $('#loadMore').click(function () {
      x= (x+5 <= size_li) ? x+5 : size_li;
      $('#loade ('+x+')').show();
  });

});
