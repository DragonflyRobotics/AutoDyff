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

function checkAnswer(value) {
    equationsubmitted = value;
    console.log(value);
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
    autoOperatorNames: 'sin cos',
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
        }
    };

    xhttp.open("POST", "https://codermerlin.academy/vapor/krishna-shah/numerical_engine/endpoint_latex");

    xhttp.send(stringify); 
}
