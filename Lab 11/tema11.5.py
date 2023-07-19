# 5. a) La fel ca la problema 3, dar nu folosim os.walk() ci ne creem noi o functie recursiva care are un parametru
# string care va fi folderul de start și care afișează fișierele .py din acel folder iar pentru subfoldere intra în
# recursivitate, afisand tot așa fisierele .py. b) La fel ca la problema 4, dar nu folosim os.walk() ci ne creem noi
# o functie recursiva care are un parametru string care va fi folderul de start și care returneaza dimensiunea totala
# a fișierelor din acel folder (din tot arborele care porneste de la acel folder mai exact)
print('Tema 11.5a')
import os


def show_python_files(p):
    if os.path.isfile(p):
        if p.lower().split('.')[-1] == 'py':
            print(p)
    else:
        for f in os.listdir(p):
            show_python_files(os.path.join(p, f))


start_dir = 'C:\\Users\\Ana\\Desktop\\Python'  # replace this with your local dir
show_python_files(start_dir)
print('Tema 11.5a')
import os


def get_size(p):
    if os.path.isfile(p):
        return os.path.getsize(p)
    else:
        size = 0
        for f in os.listdir(p):
            size += get_size(os.path.join(p, f))
        return size


start_dir = 'C:\\Users\\Ana\\Desktop\\Python'  # replace this with your local dir
print('Path: ', start_dir)
print('Total size: ', get_size(start_dir))
