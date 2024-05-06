// Get the form element with id "input"
const form = document.getElementById("input");

// Add an event listener to the form that triggers the onFormSubmit function when the form is submitted
form.addEventListener("submit", onFormSubmit);

// Initialize a variable to hold the equation submitted by the user
var equationsubmitted = "";

// Function that is called when the form is submitted
function onFormSubmit(event) {
    // Prevent the form from being submitted normally
    event.preventDefault();

    // Create a FormData object from the form
    const data = new FormData(event.target);

    // Convert the FormData to a regular object
    const dataObject = Object.fromEntries(data.entries());

    // Add the submitted equation to the data object
    dataObject['equation'] = equationsubmitted;

    // Call the calc function with the data object converted to a JSON string
    calc(JSON.stringify(dataObject));
}

// Function to check if a string is a valid math equation
function isValidMath(mathString) {
    // Use MathQuill's internal methods to check if the math string is valid
    try {
        // If the string can be converted to a MathQuill latex string, it is valid
        MQ.MathField().latex(mathString);
        return true;
    } catch (error) {
        // If an error is thrown, the string is not valid
        console.log(error);
        return false;
    }
}

// Function to check the user's answer
function checkAnswer(value) {
    // Store the submitted equation
    equationsubmitted = value;

    // Log the submitted equation
    console.log(value);

    // Check if the submitted equation is valid
    if (!isValidMath(value)) {
        // If the equation is not valid, log an error message
        console.log('Error: Invalid equation');
    } else {
        // If the equation is valid, log an empty string
        console.log('');
    } 
}

// Get the span element with id 'equation'
var answerSpan = document.getElementById('equation');

// Create a MathQuill math field with the span element
var answerMathField = MQ.MathField(answerSpan, {
    // Configure the behavior of the math field
    spaceBehavesLikeTab: true,
    leftRightIntoCmdGoes: 'up',
    restrictMismatchedBrackets: true,
    sumStartsWithNEquals: true,
    supSubsRequireOperand: true,
    charsThatBreakOutOfSupSub: '+-=<>',
    autoSubscriptNumerals: true,
    autoCommands: 'pi sqrt',
    autoOperatorNames: 'sin cos tan ln log arcsin arccos arctan cot csc sec sinh cosh tanh arccsc arcsec arccot sigmoid',
    maxDepth: 10,
    // Replace the textarea used by MathQuill with a new textarea element
    substituteTextarea: function() {
        return document.createElement('textarea');
    },
    // Add an event handler for when the math field is edited
    handlers: {
        edit: function() {
            // Get the entered math in LaTeX format
            var enteredMath = answerMathField.latex();

            // Check the entered math
            checkAnswer(enteredMath)
        }
    }
});

// Function to send a POST request to the server with the submitted equation
function calc(stringify) {
    // Create a new XMLHttpRequest object
    const xhttp = new XMLHttpRequest();

    // Add an event listener for when the state of the request changes
    xhttp.onreadystatechange = function() {
        // Check if the request is done and was successful
        if (this.readyState == 4 && this.status == 200) {
            // Parse the response text as JSON
            console.log(JSON.parse(this.responseText))

            // Update the HTML elements with the response data
            document.getElementById("f_x").innerHTML = JSON.parse(this.responseText)['f'];
            document.getElementById("f_prime_x").innerHTML = JSON.parse(this.responseText)['f_prime'];
            document.getElementById("error").innerHTML = JSON.parse(this.responseText)['error'];

            // Fetch the image from the server
            fetch('get_image')
                .then(response => response.json())
                .then(data => {
                    // Update the image element with the fetched image
                    document.getElementById('myImage').src = 'data:image/jpeg;base64,' + data.image;
                });
        }
    };

    // Open the request with the POST method and the URL of the server endpoint
    xhttp.open("POST", "numerical_engine/endpoint_latex");

    // Send the request with the JSON string as the body
    xhttp.send(stringify); 
}
