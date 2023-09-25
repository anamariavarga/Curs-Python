function verify() {
    // Resetarea mesajelor de avertizare
    document.getElementById("usernameEroare").innerText = "";
    document.getElementById("parolaEroare").innerText = "";
    document.getElementById("confirmareParolaEroare").innerText = "";

    // Obținerea valorilor introduse în câmpuri
    var username = document.getElementById("username").value;
    var parola = document.getElementsByName("parola")[0].value;
    var confirmareParola = document.getElementsByName("confirmare parola")[0].value;

    // Verificare pentru username
    if (username.length < 4 || username.length > 10) {
        document.getElementById("usernameEroare").innerText = "Username trebuie să aibă între 4 și 10 caractere.";
        document.getElementById("usernameEroare").style.color = "red";
        return false; // Împiedică trimiterea formularului
    ,2000}

    // Verificare pentru parolă
    if (parola.length < 8 || parola.length > 20) {
        document.getElementById("parolaEroare").innerText = "Parola trebuie să aibă între 8 și 20 de caractere.";
        document.getElementById("parolaEroare").style.color = "red";
        return false; // Împiedică trimiterea formularului
    ,2000}

    // Verificare pentru confirmarea parolei
    if (parola !== confirmareParola) {
        document.getElementById("confirmareParolaEroare").innerText = "Confirmarea parolei nu corespunde cu parola introdusă.";
        document.getElementById("confirmareParolaEroare").style.color = "red";
        return false; // Împiedică trimiterea formularului
    ,2000}

    // Dacă toate condițiile sunt îndeplinite, formularul va fi trimis
    return true;
}

