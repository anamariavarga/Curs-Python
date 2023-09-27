function validare_campuri() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var mesaj = document.getElementById("mesaj").value;
//    var outputVal = document.getElementById("error-message");

    if (name == '' || email == '' || mesaj) {
        alert("Toate campurile trebuiesc completate");
        return false;
    }

}


//    if (nameField === '' || emailField === '') {
//        outputVal.style.color = "red";
//        outputVal.innerHTML = "Toate câmpurile trebuie completate";
//    } else {
//        outputVal.style.color = "green";
//        outputVal.innerHTML = "Formularul este completat";
//        }
//
//    }
//    return false;
//}