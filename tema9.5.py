# 5. Ne uităm la rezolvările din temele precedente acolo unde extrăgeam pe cei trei premianți din rândul elevilor.
# Acum trebuie sa le pregătim și câte o diplomă frumoasă. :-)
# Diploma va arăta cam așa: Se acorda premiul I pentru
# rezultate deosebite la învățătură elevului/elevei Bengescu Hortensia Media de absolvire: 9.45
# Vor fi trei astfel de texte pe care le vom salva în câte un fișier cu numele,
# premiu-1.txt,
# premiu-2.txt,
# premiu-3.txt.
# Ne amintim de modalitățile de formatare ale textelor și folosim aici pe care dorim.
# Șablonul pentru diploma as vrea sa fie stocat
# într-un fișier text
# diploma.txt
# cu următorul conținut și de acolo sa cititi textul, nu sa îl aveți direct în
# program într-o variabila.
# Îl aduceți din fișier.
# Șablonul pentru diplomă este: Se acorda premiul {} pentru
# rezultate deosebite la învățătură elevului/elevei {} Media de absolvire: {}
# Variațiune la tema asta: încercați sa vedeți dacă puteți genera diplomele în fișiere docx.
# Cautati pe Google, pypi.org vreun modul care sa permita
# generarea de fisiere docx, instalați-l și generați cu el diplomele în format docx. Va trebui sa studiati un pic
# documentația unui astfel de modul dacă exista (și probabil ca exista :-) )
champs = {
    'Bengescu Hortensia': 9.16,
    'Vasilescu Vasile': 9.00,
    'Ionescu Geta': 8.34,
}

with open('diploma.txt', 'r') as file:
    diploma = file.read()

for i, e in enumerate(sorted(champs, key=champs.get, reverse=True), start=1):
    with open(f'premiu-{i}.txt', 'w') as file:
        print(diploma.format(i * 'I', e, champs[e]), file=file)
print("**************************************************************")
# first install docxtpl
# https://docxtpl.readthedocs.io/en/latest/
from docxtpl import DocxTemplate

champs = {
    'Bengescu Hortensia': 9.16,
    'Vasilescu Vasile': 9.00,
    'Ionescu Geta': 8.34,
}

doc = DocxTemplate("diploma.docx")

for i, e in enumerate(sorted(champs, key=champs.get, reverse=True), start=1):
    context = {'e': e, 'p': i * 'I', 'm': champs[e]}
    doc.render(context)
    doc.save(f'Premiu-{i}.docx')