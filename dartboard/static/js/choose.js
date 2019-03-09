var number = -1;
var state = 0;
var doingStuff = 0;

function requestHeartbeat() {
  $.ajax({
    type: 'GET',
    url: "http://100.64.13.129/heartbeat",
    error: AjaxFailed,
    success: function(data) {
      doingStuff = 0;
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
      doingStuff = 0;
    },
    data: {
      maxNum: options.length
    },
    dataType: "text",
    async: false,
  });
}

function AjaxFailed(result) {
  //alert("hello1");
  alert(result.status + ' ' + result.statusText);
}

switch (state) {
  case 0:
    doingStuff = 1;
    requestHeartbeat();
    state = 1;
    break;
  case 1:
    if (doingStuff == 0) {
      state = 2;
    }
    break;
  case 2:
    doingStuff = 1;
    requestThrow();
    state = 3;
    break;
  case 3:
    if (doingStuff == 0) {
      state = 4;
    }
    break;
  case 4:
    window.alert(options[number])
    state = 5;
    break;
}
