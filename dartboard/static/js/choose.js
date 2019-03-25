var number = -1;
var state = 0;
var doingStuff = 0;
var state = 0;
var dots = $('.dots');
var waiting = true;

function requestHeartbeat() {
  $.ajax({
    type: 'GET',
    url: "http://henryocallaghan.pagekite.me/heartbeat/",
    error: AjaxFailed,
    success: function(data) {
      if (waiting === true) {
        dots.text("");
        text.text('Throw!')
        state = 1;
        requestThrow();
      }
    }
  });
}

function requestThrow() {
  $.ajax({
    type: 'GET',
    url: "http://henryocallaghan.pagekite.me/getNum/",
    error: AjaxFailed,
    success: function(data) {
      if (waiting === true) {
        state = 2;
        number = JSON.parse(data)["num"];
        var answer = options[number];
        text.text('Your answer is ' + answer + '!');
      }
    },
    data: {
      "maxNum": options.length
    },
    dataType: "text",
    //timeout: 10000, // sets timeout to 3 seconds
  });
}

function skipThrow() {
  waiting = false;
  state = 2;
  dots.text("");
  var x = document.getElementById(1);
  x.style.display = "none";
  var number = getRandomInt(0, options.length - 1);
  var answer = options[number];
  text.text('Your answer is ' + answer + '!');
}

function AjaxFailed(result) {
  //alert("hello1");
  dots.text("");
  text.text(result);
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

/**
 * Returns a random integer between min (inclusive) and max (inclusive).
 * The value is no lower than min (or the next integer greater than min
 * if min isn't an integer) and no greater than max (or the next integer
 * lower than max if max isn't an integer).
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var text = $('.choose-text');
text.text('Waiting for heartbeat')
requestHeartbeat();
