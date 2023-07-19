# 3. Pornind de la o cale existenta de pe unitatea voastra de stocare (de exemplu directorul unde aveți structura de
# fișiere Python) parcurgeti cu os.walk() calea respectivă și afișați una sub alta toate fișierele python (care au
# extensia .py) precum și numărul lor total. E posibil sa fie și fișiere python cu extensia .PY sau .Py. As vrea sa
# fie afișate indiferent de case-ul folosit. Exemplu de output: C:/user/workspace/lab01/tema1.py
# C:/user/workspace/lab02/modules/my_module.PY C:/user/workspace/lab05/some-file.Py Nr. python files: 3
import os

no_dirs = 0
no_files = 0

for root, dirs, files in os.walk('C:\\Users\\Ana\\PycharmProjects\\folder pentru tema 11.3'):

    for file in files:
        # if file.lower().endswith('.py'):  # varianta 1
        # if file.split('.')[-1].lower() == "py": # varianta 2
        if file[-3:].lower()==".py":
            no_files += 1
            print(os.path.join(root, file))
            print(no_files)

print('Nr. Python files: ', no_files)

print('........................................')
import os

nr_python_files = 0
start_dir = '/'  # replace this with your local dir

for root, dirs, files in os.walk(start_dir):
    for file in files:
        if file.lower().split('.')[-1] == 'py':
            nr_python_files += 1
            print(f'{root}/{file}')

print('Nr. python files:', nr_python_files)

