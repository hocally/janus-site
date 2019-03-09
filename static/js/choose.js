var number = -1;
var state = 0;
var doingStuff = 0;

function requestHeartbeat() {
  $.ajax({
    type: 'GET',
    url: "http://100.64.13.129/heartbeat",
    error: AjaxFailed,
    success: function(data) {
      text.text('Throw!')
      requestThrow();
    }
  });
}

function requestThrow() {
  $.ajax({
    type: 'POST',
    url: "http://100.64.13.129/numberRequest",
    error: AjaxFailed,
    success: function(data) {
      number = data;
      var answer = options[number];
      text.text('The dartboard has spoken: your answer is ' + answer + '!');
    },
    data: {
      maxNum: options.length
    },
    dataType: "text",
  });
}

function AjaxFailed(result) {
  //alert("hello1");
  text.text('Error: Cannot commuinicate with microcontroller!');
}

/*
setInterval(function() {
    var th = $('.dots');
    if(th.text().length < 3){
        th.text(th.text()+".");
    }else{
        th.text("");
    }
}, 500);
*/
var text = $('.choose-text');
text.text('Waiting for heartbeat...')
requestHeartbeat();
