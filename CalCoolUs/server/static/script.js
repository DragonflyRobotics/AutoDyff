const form = document.getElementById("input");
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
        console.log(JSON.parse(this.responseText))
        document.getElementById("f_x").innerHTML = JSON.parse(this.responseText)['f']; // This console logs the output, just change it to whatever.
        document.getElementById("f_prime_x").innerHTML = JSON.parse(this.responseText)['f_prime']; // This console logs the output, just change it to whatever.
    }
  };
  xhttp.open("POST", "https://codermerlin.academy/vapor/brennan-coil/numerical_engine/endpoint");
  
  xhttp.send(stringify); 
}
