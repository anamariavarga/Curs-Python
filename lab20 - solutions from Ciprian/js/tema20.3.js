function factorial(n) {
    let f = 1
    for (let i = 2; i <= n; i++) {
        f *= i
    }
    return f
}

function valideaza() {
    let v = parseInt(document.getElementById('number').value)
    let r = document.getElementById('results')
    if (! isNaN(v) && v > 0) {
        r.style.color = 'green'
        r.innerHTML = "Factorialul numarului introdus este: " + factorial(v)
    } else {
        r.style.color = 'red'
        r.innerHTML = "Nu se poate calcula factorialul"
    }
}