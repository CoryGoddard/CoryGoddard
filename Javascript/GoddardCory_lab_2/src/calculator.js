
// constant for resultbutton, add event listener to calculate/display side c
const resultButton = document.getElementById("result");
resultButton.addEventListener("click", pythagorean);

// Calculates side c using the pythagorean formula
function pythagorean() {
    let sideA = document.getElementById("sideA");                 // get value of side a
    if (sideA.value <= 0) {                                       // display an alert if side a is less than or equal to 0
        alert("You must have a value greater than 0 for Side A.");
        return;
    }
    
    let sideB = document.getElementById("sideB");                 // get value of side b
    if (sideB.value <= 0) {                                       // display an alert if side b is less than or equal to 0
        alert("You must have a value greater than 0 for Side B.");
        return
    }

    let sideC = document.getElementById("solution");
    let c = Math.sqrt(sideA.value**2 + sideB.value**2);           // calculate the length of side c, then display it
    sideC.innerHTML = "Side C:<br /><input type=\"number\" value = \"" + parseFloat(c.toFixed(4)) + "\" readonly/>";
   
    // reset side a and b text fields
    sideA.value = "";
    sideB.value = "";
};