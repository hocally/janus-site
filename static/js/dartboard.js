var i;
var j;
var k;
var num = 0;
var list = [];

var colors = {};
for(i = 0; i < options.length; i++) {
  colors[i] = [];
}

fillList();

for (i = 1; i <= 20; i++) {
  var tile = "s" + chooseFromList();
  var temp = colors[num];
  temp.push(tile)
  colors[num] = temp
  var s = document.getElementById(tile);
  s.style.fill = getColor(num);
  num = num + 1;
  if (num >= options.length) {
    num = 0;
  }
}

fillList();

for (i = 1; i <= 20; i++) {
  var tile = "t" + chooseFromList();
  var temp = colors[num];
  temp.push(tile)
  colors[num] = temp
  var s = document.getElementById(tile);
  s.style.fill = getColor(num);
  num = num + 1;
  if (num >= options.length) {
    num = 0;
  }
}

fillList();

for (i = 1; i <= 20; i++) {
  var tile = "d" + chooseFromList();
  var temp = colors[num];
  temp.push(tile)
  colors[num] = temp
  var s = document.getElementById(tile);
  s.style.fill = getColor(num);
  num = num + 1;
  if (num >= options.length) {
    num = 0;
  }
}

function getColor(num) {
  switch (num) {
    case 0:
      return "red";
      break;
    case 1:
      return "blue";
      break;
    case 2:
      return "orange";
      break;
    case 3:
      return "purple";
      break;
    case 4:
      return "white";
      break;
    case 5:
      return "black";
      break;
    case 6:
      return "green";
      break;
    case 7:
      return "yellow";
      break;
    case 8:
      return "magenta";
      break;
    case 9:
      return "teal";
      break;
    default:
      return "white";
  }
}

function chooseFromList() {
  var result = list[Math.floor(Math.random() * list.length)];
  var index = list.indexOf(result);
  if (index !== -1) {
    list.splice(index, 1);
  }
  return result;
}

function fillList() {
  for (var i = 1; i <= 20; i++) {
    list.push(i);
  }
}
