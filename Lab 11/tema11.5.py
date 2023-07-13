# 5. a) La fel ca la problema 3, dar nu folosim os.walk() ci ne creem noi o functie recursiva care are un parametru
# string care va fi folderul de start și care afișează fișierele .py din acel folder iar pentru subfoldere intra în
# recursivitate, afisand tot așa fisierele .py. b) La fel ca la problema 4, dar nu folosim os.walk() ci ne creem noi
# o functie recursiva care are un parametru string care va fi folderul de start și care returneaza dimensiunea totala
# a fișierelor din acel folder (din tot arborele care porneste de la acel folder mai exact)
print('Tema 11.5a')
import os

no_dirs = 0
no_files = 0

for root, dirs, files in os.walk('C:\\Users\\Ana\\PycharmProjects\\folder pentru tema 11.3'):

    for file in files:
        if file.lower().endswith('.py'):
            no_files += 1
            print(os.path.join(root, file))

print('Nr. Python files: ', no_files)
print('Tema 11.5b')
import os

no_dirs = 0
no_files = 0
total_size = 0

for root, dirs, files in os.walk('C:\\Users\\Ana\\Desktop\\Python'):
    no_dirs += len(dirs)
    no_files += len(files)
    file_size = os.path.getsize(root)
    print('Start dir:  ', root)
    total_size += file_size

print('Total file size: ', total_size, 'bytes')