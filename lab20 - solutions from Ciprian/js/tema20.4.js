function valideaza() {
    let u = document.getElementById('username')
    let p = document.getElementById('password')
    let pc = document.getElementById('password_conf')
    let u_m = document.getElementById('div_username')
    let p_m = document.getElementById('div_password')
    let pc_m = document.getElementById('div_password_conf')

    if (u.value.length >= 4 && u.value.length <= 10) {
        u_m.innerHTML = ''
    } else {
        u_m.innerHTML = 'Dimensiunea campului trebuie sa fie intre 4 si 10 caractere'
    }

    if (p.value.length >= 8 && u.value.length <= 20) {
        p_m.innerHTML = ''
    } else {
        p_m.innerHTML = 'Dimensiunea campului trebuie sa fie intre 8 si 20 caractere'
    }

    if (p.value != pc.value) {
        pc_m.innerHTML = 'Parolele nu contin aceeasi valoare'
    } else {
        pc_m.innerHTML = ''
    }
}