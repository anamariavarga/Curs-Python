function validare_campuri() {
    var nameField = document.getElementById('name').value;
    var emailField = document.getElementById('email').value;
    var errorMessage = document.getElementById('error-message');

    if (nameField === '' || emailField === '' || mesajField === '') {
        errorMessage.textContent = 'Toate câmpurile trebuie completate.';
        return false; // Opriți trimiterea formularului
    }

    // Dacă toate câmpurile sunt completate, permiteți trimiterea formularului
    return true;
}


