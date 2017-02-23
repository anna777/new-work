$(document).ready(function () {
    
    size_li = $("#load tr").size();
    x=1;
    $('#load tr:lt('+x+')').show();
    $('#loadMore').click(function () {
        x= (x+1 <= size_li) ? x+1 : size_li;
        $('#load tr:lt('+x+')').show();
    });
    $('#showLess').click(function () {
        x=(x-1<0) ? 1 : x-1;
        $('#load tr').not(':lt('+x+')').hide();
    });
});
