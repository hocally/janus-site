
var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }
        anHttpRequest.open("GET", aUrl, false);
        anHttpRequest.send();
    }
}

function recieveHeartbeat(response) {
  window.alert("Heartbeat: " + response);
}

function recieveValue(response) {
  window.alert("Randomnumber: " + response);
}
var client = new HttpClient();
client.get('http://100.64.13.129/heartbeat', recieveHeartbeat);
client.get('http://100.64.13.129/numberRequest', recieveValue);


/*
function makeHttpObject() {
  try {return new XMLHttpRequest();}
  catch (error) {}
  try {return new ActiveXObject("Msxml2.XMLHTTP");}
  catch (error) {}
  try {return new ActiveXObject("Microsoft.XMLHTTP");}
  catch (error) {}

  throw new Error("Could not create HTTP request object.");
}

var request = makeHttpObject();
request.open("GET", "http://100.64.13.129/heartbeat", false);
request.send();
window.alert(request.getAllResponseHeaders());
*/
//
/*
$.ajax({
  url: "http://100.64.13.129/heartbeat",
  error: AjaxFailed,
  success: function(data) {
    window.alert(data);
    //do something when request is successfull
  },
  dataType: "text"
});

//

$.get(
  "http://100.64.13.129/heartbeat",
  function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
  });

function AjaxFailed(result) {
    //alert("hello1");
    alert(result.status + ' ' + result.statusText);
}
*/
