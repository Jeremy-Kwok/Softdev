// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

//give an alert using the content of whatever is clicked
var clicky = function(e) {
  alert( this.innerHTML );
};

//Loop through every single cell and add event listener
for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

//