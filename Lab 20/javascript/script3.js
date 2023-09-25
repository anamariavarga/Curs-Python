function formular() {
    var inputVal = document.getElementById("numar").value;
    var outputVal = document.getElementById("rezultat");

    if (isNaN(parseInt(inputVal)) || parseInt(inputVal) < 0) {
        outputVal.style.color = "red";
        outputVal.innerHTML = "Nu se poate calcula factorialul";
    } else {
        var factorial = 1;
        for (var i = 1; i <= parseInt(inputVal); i++) {
            factorial *= i;
        }
        outputVal.style.color = "green";
        outputVal.innerHTML = "Factorialul numarului introdus este: F = " + factorial;
    }
    return false;
}

