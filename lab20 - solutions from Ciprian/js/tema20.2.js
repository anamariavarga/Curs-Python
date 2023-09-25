function valideaza() {
    v = parseInt(document.getElementById('number').value)
    if (isNaN(v)) {
        document.getElementById('results').innerHTML = "Valoarea introdusa nu poate fi convertita la un numar."
    } else {
        document.getElementById('results').innerHTML = "Valoarea numerica extrasa este: " + v
    }
}