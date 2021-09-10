
function fade() {
  $(this)
    .fadeOut(50)
    .fadeIn(200)
  ;
}

function addToScreen() {
  $(this)
    $('#screen').append($(this).data('val'))
  ;
}

function clearScreen() {
  $(this)
    $('#screen').empty()
  ;
}

function sendToServer() {
  $(this)
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
    }
    xhttp.open("POST", "demo_post2.asp");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send($('#screen').text());
  ;
}

$('.button, .operator, .cls').on('click', fade);
$('.button, .operator').on('click', addToScreen);
$('.cls').on('click', clearScreen);
$('.sendToServer').on('click', sendToServer);
