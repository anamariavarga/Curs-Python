# 4. Pe un server pe care îl administrăm trebuie sa fim atenți la spațiul ocupat de un anumit director. Pentru asta
# trebuie sa scriem un program care pornind de la acel director (cu os.walk()) contorizează dimensiunea totala a
# tuturor fișierelor din acel director. Va trebui sa descoperiți care functionalitate din os sau alt modul (submodul
# din os) ne da dimensiunea unui fișier și apoi sa adunati dimensiunile la un contor general. Exemplu de output:
# Start dir: C:/user/Documents Total file size: 12345678
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
