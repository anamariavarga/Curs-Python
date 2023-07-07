# 4. Scrieti o functie care calculeaza media generala a clasei. Practic aceasta este media tuturor mediilor elevilor. Încercați sa
# refolositi funcția de calcul a mediei de data trecută.
def media(p):
    if len(p) > 0:
        return  round(sum(p)/len(p),2)
    else:
        return 0

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
medii = []
for k, v in catalog.items():
    medii.append((media(v)))

for k in catalog:
    medii.append(media(catalog[k]))

print(media(medii))
print('............................................................')
medii={}
for k in catalog:
    medii[k] = media(catalog[k])
m=0
print(medii)
for k in medii:
    m += medii[k]
me = round(m/len(medii),2)
print(me)
