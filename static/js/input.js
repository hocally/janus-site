var currentShown = 2;

function showNext() {
  if (currentShown < 10) {
    var i = currentShown + 1;
    var x = document.getElementById(i);
      x.style.display = "";

    currentShown += 1;
    if (currentShown === 10) {
      x = document.getElementById(11);
      x.style.display = "none";
    }
  } else {
    window.alert("Uh Oh")
  }
}


function setup() {
  for (i = 1; i <= 2; i++) {
    var x = document.getElementById(i);
    x.style.display = "";
  }
}

setup();
