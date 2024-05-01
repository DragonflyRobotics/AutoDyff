const form = document.getElementById("input");
form.addEventListener("submit", onFormSubmit);
var equationsubmitted = "";

function onFormSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);
    const dataObject = Object.fromEntries(data.entries());
    dataObject['equation'] = equationsubmitted;
    calc(JSON.stringify(dataObject));
}

function isValidMath(mathString) {
    // Use MathQuill's internal methods to check if the math string is valid
    try {
        MQ.MathField().latex(mathString);
        return true;
    } catch (error) {
        console.log(error);
        return false;
    }
}

function checkAnswer(value) {
    equationsubmitted = value;
    console.log(value);
    if (!isValidMath(value)) {
        console.log('Error: Invalid equation');
    } else {
        console.log('');
    } 
}

var answerSpan = document.getElementById('equation');
var answerMathField = MQ.MathField(answerSpan, {
    spaceBehavesLikeTab: true,
    leftRightIntoCmdGoes: 'up',
    restrictMismatchedBrackets: true,
    sumStartsWithNEquals: true,
    supSubsRequireOperand: true,
    charsThatBreakOutOfSupSub: '+-=<>',
    autoSubscriptNumerals: true,
    autoCommands: 'pi theta sqrt',
    autoOperatorNames: 'sin cos tan ln log arcsin arccos arctan cot csc sec sinh cosh tanh arccsc arcsec arccot sigmoid sqrt',
    maxDepth: 10,
    substituteTextarea: function() {
        return document.createElement('textarea');
    },
    handlers: {
        edit: function() {
            var enteredMath = answerMathField.latex(); // Get entered math in LaTeX format
            checkAnswer(enteredMath)
        }
    }
});


function calc(stringify) {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(JSON.parse(this.responseText))
            document.getElementById("f_x").innerHTML = JSON.parse(this.responseText)['f']; // This console logs the output, just change it to whatever.
            document.getElementById("f_prime_x").innerHTML = JSON.parse(this.responseText)['f_prime']; // This console logs the output, just change it to whatever.
            document.getElementById("error").innerHTML = JSON.parse(this.responseText)['error']; // This console logs the output, just change it to whatever.
        fetch('/vapor/brennan-coil/get_image')
            .then(response => response.json()
                )
            .then(data => {
                document.getElementById('myImage').src = 'data:image/jpeg;base64,' + data.image;
            });
        }
    };

    xhttp.open("POST", "/vapor/brennan-coil/numerical_engine/endpoint_latex");

    xhttp.send(stringify); 
}
