print("Exercitiul 3.5")
newList = ['in', 'livada', 'noastra', 'avem', 'ciresi', 'meri', 'peri', 'si', 'pruni', 'care', 'fructe', 'credeti',
           'ca', 'se', 'coc', 'primele', 'variante', 'perele', 'merele', 'prunele', 'si', 'apoi', 'ciresele', 'foarte',
           'gresit', 'corect', 'este', 'ciresele', 'merele', 'perele', 'si', 'apoi', 'prunele']

print("a. cuvintele din lista sa nu se repete")
newList = list(dict.fromkeys(newList))
print(newList)


print("b. se sorteaza alfabetic lista de stringuri")
newList.sort()
print(newList)

print("c.Se creeaza programul care sorteaza lista")

newnew =[]
for e in range(len(newList)):
    e = min(newList)
    newnew.append(newList.pop(newList.index(e)))
print(newnew)
print("......................................................................")
l2 = ['in', 'livada', 'noastra', 'avem', 'ciresi', 'meri', 'peri', 'si', 'pruni', 'care', 'fructe', 'credeti',
           'ca', 'se', 'coc', 'primele', 'variante', 'perele', 'merele', 'prunele', 'si', 'apoi', 'ciresele', 'foarte',
           'gresit', 'corect', 'este', 'ciresele', 'merele', 'perele', 'si', 'apoi', 'prunele']
one_more = True
while one_more:
    one_more = False
    for i in range(len(l2)-1):
        if l2[i] > l2[i+1]:
            l2[i],l2[i+1]=l2[i+1],l2[i]
            one_more = True
print(newList)