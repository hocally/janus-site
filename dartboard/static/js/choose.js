var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.response);
        }
        anHttpRequest.open("GET", aUrl, true);
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
//client.get('http://100.64.13.129/', recieveHeartbeat);
client.get('https://www.random.org/integers/?num=1&min=1&max=5&col=1&base=10&format=plain&rnd=new', recieveValue);
