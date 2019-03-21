var number = -1;
var state = 0;
var doingStuff = 0;
var state = 0;
var dots = $('.dots');


function requestHeartbeat() {
  $.ajax({
    type: 'GET',
    url: "http://henryocallaghan.pagekite.me/heartbeat/",
    error: AjaxFailed,
    success: function(data) {
      dots.text("");
      text.text('Throw!')
      state = 1;
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
      state = 2;
      number = JSON.parse(data)["num"];
      var answer = options[number];
      text.text('Your answer is ' + answer + '!');
    },
    data: {
      "maxNum": options.length
    },
    dataType: "text",
    //timeout: 10000, // sets timeout to 3 seconds
  });
}

function AjaxFailed(result) {
  //alert("hello1");
  dots.text("");
  text.text('Error: Cannot commuinicate with microcontroller!');
  state = -1;

}
setInterval(function() {
  if (state == 0) {
    if (dots.text().length < 3) {
      dots.text(dots.text() + ".");
    } else {
      dots.text("");
    }
  }
}, 500);


var text = $('.choose-text');
text.text('Waiting for heartbeat')
requestHeartbeat();
