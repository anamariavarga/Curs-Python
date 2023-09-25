function formular() {
    var inputVal = document.getElementById("numar").value;
    var outputVal = document.getElementById("rezultat");

    if (isNaN(parseInt(inputVal))) {
        outputVal.innerHTML = "Valoarea introdusa nu poate fi convertita la un numar.";
    } else {
        outputVal.innerHTML = "Valoarea numerica extrasa este: " + parseInt(inputVal);
    }
    return false;
}