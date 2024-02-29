const form = document.getElementById("my-form");
form.addEventListener("submit", onFormSubmit);


function onFormSubmit(event) {
	event.preventDefault();
	const data = new FormData(event.target);
	const dataObject = Object.fromEntries(data.entries());
	calc(JSON.stringify(dataObject));
}

function calc(stringify) {
  const xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("output").innerHTML = this.responseText; // This console logs the output, just change it to whatever.
    }
  };
  xhttp.open("POST", "/numerical_engine/endpoint");
  
  xhttp.send(stringify); 
}
