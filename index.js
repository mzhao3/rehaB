
// screen
/**
var c = document.getElementsByClassName("background")[0];
console.log(c);
var ctx = c.getContext("2d");
**/
var requestID;
// array of words
var array;
//==============================================================================
var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var letters = [];

var hive = Array.from(document.getElementsByClassName("hive")[0].children)
console.log(hive);

for (i = 0; i < hive.length; i+= 1) {
  var letter = pickRandomLetter();
  hive[i].innerHTML = letter;
  letters.push(letter);
}

function pickRandomLetter() {
  var index = Math.floor (Math.random()* 25);
  return alphabet[index];
}

//==============================================================================
/**
function validWord(word) {
  //if word in dict --> return true
  //if word not in dict --> return false
}
**/
var guess = document.getElementsByClassName("guesses")[0];
guess.addEventListener('keydown', function (e)  {
  if (event.which == 13 || event.keyCode == 13) {
        //code to execute here
        e.preventDefault();
        return false;
    }
    return true;
});


function results() {
  console.log("hey there");
  console.log(guess)
}
var nameValue = document.getElementById("hi").value;
console.log(nameValue)
console.log("gibberish")
function myFunction() {
  var x = guess.value;
  document.getElementById("ii").innerHTML = x;
}
//==============================================================================
/**
var clear = function() {
  ctx.clearRect(0, 0, c.width, c.height);
}

var stopIt = function() {
  window.cancelAnimationFrame(requestID);
};


// move from textbox into cookie jar
var moveWord = function(id) {
  window.cancelAnimationFrame(requestID);

  // reaches cookiejar
  if (y = ?? ) {
    stopIt();
  } else {
    y += 1;
  }
  clear();
  //word is a placeholder here
  var wordBox = word.toDataURL;
  // put image into the array of words
  ctx.drawImage(wordBox, x, y, width = 30, height = 10);
  requestID = window.requestAnimationFrame(moveWord);

}

//==============================================================================
var cookieJar = document.getElementbyId("cookiejar");
cookieJar.addEventListener('click', function(e) {
  //go to next screen
}

var spread_the_words = function (array) {
  for (i = 0; i < (numwords); i+=1 ) {
    var word = array[i];
    word.addEventListener('click', somefunction);
    word.addEventListener('hover', somethingelse);
    //set up flex box
    word.style.flex = "25%";
  }
}
**/
