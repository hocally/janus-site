var number = -1;
var state = 0;
var doingStuff = 0;

function requestHeartbeat() {
  $.ajax({
    type: 'GET',
    url: "http://henryocallaghan.pagekite.me/heartbeat/",
    error: AjaxFailed,
    success: function(data) {
      text.text('Throw!')
      requestThrow();
    }
  });
}

function requestThrow() {
  $.ajax({
    type: 'GET',
    url: "http://henryocallaghan.pagekite.me/getNum/",
    error: AjaxFailed,
    success: function(data) {
      number = JSON.parse(data)["num"];
      var answer = options[number];
      text.text('The dartboard has spoken: your answer is ' + answer + '!');
    },
    data: {
      "maxNum": options.length
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
