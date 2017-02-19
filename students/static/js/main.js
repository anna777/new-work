$(document).ready(function () {
    $("tbody tr").hide();
    size_li = $("tbody tr").size();
    x=1;
    $('tbody tr:lt('+x+')').show();
    $('#loadMore').click(function () {
        x= (x+1 <= size_li) ? x+1 : size_li;
        $('tbody tr:lt('+x+')').show();
    });
    $('#showLess').click(function () {
        x=(x-1<0) ? 1 : x-1;
        $('tbody tr').not(':lt('+x+')').hide();
    });
});
