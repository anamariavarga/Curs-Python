# 2. Pornind de la o cale existenta de pe unitatea voastra de stocare (de exemplu C:/user/workspace) parcurgeti cu
# os.walk() calea respectiva și contorizati toate fisierele și directoarele care se afla în structura arborescenta
# care porneste de la calea respectiva. Programul va afisa doua numere: numarul total de fisiere și numarul total de
# directoare. Exemplu de output: Path: C:/user/workspace Nr. folders: 14 Nr. files: 53
import os

no_dirs = 0
no_files = 0

for root, dirs, files in os.walk('C:\\Users\\Ana\\Desktop\\Python'):
    no_dirs += len(dirs)
    no_files += len(files)
    print('Path: ', root)
print('Nr. folders: ', no_dirs)
print('Nr. files: ', no_files)
