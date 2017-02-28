function loadMore () {
    $("#load tr").slice(0, 4).show();
    size_li = $("#load tr").size();
    x=4;
    $('#load tr:lt('+x+')').show();
    $('#loadMore').click(function () {
        x= (x+2 <= size_li) ? x+2 : size_li;
        $('#load tr:lt('+x+')').show();
    });
    $('#showLess').click(function () {
        x=(x-1<0) ? 1 : x-1;
        $('#load tr').not(':lt('+x+')').hide();
    });
};



function initJournal() {
  var indicator = $('#ajax-progress-indicator');

  $('.day-box input[type="checkbox"]').click(function(event){
    var box = $(this);
    $.ajax(box.data('url'), {
      'type': 'POST',
      'async': true,
      'dataType': 'json',
      'data': {
        'pk': box.data('student-id'),
        'date': box.data('date'),
        'present': box.is(':checked') ? '1': '',
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      'beforeSend': function(xhr, settings){
        indicator.show();
      },
      'error': function(xhr, status, error){
        alert(error);
        indicator.hide();
      },
      'success': function(data, status, xhr){
        indicator.hide();
      }
    });
  });
}
function initGroupSelector() {
  // look up select element with groups and attach our even handler
  // on field "change" event
  $('#group-selector select').change(function(event){
    // get value of currently selected group option
    var group = $(this).val();

    if (group) {
      // set cookie with expiration date 1 year since now;
      // cookie creation function takes period in days
      $.cookie('current_group', group, {'path': '/', 'expires': 365});
    } else {
      // otherwise we delete the cookie
      $.removeCookie('current_group', {'path': '/'});
    }

    // and reload a page
    location.reload(true);

    return true;
  });
}

$(document).ready(function(){
loadMore();
initJournal();
initGroupSelector();
});
