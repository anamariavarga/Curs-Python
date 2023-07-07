print('''Exercitiul 2.4 - Sa se verifice daca un sir de caractere citit de la tastatura este palindrom sau nu
Se va tine cont de case-ul caracterelor''')
print('')
sirCaractere = input('Tasteaza sirul de carctere care va fi evaluat: ')
if sirCaractere == sirCaractere[::-1]:
    print("Sirul de caractere este Palindrom")
else:
    print("Sirul de caractere nu este Palindrom")
print("......................................................................................................")
sirCaractere = input('Tasteaza sirul de carctere care va fi evaluat: ')
n = len(sirCaractere)
print(n)
inv = ''  # am luat un invers, l-am considerat nul (un string gol)

i = 0
while i < n:
    inv += sirCaractere[n - i - 1]
    # cand i=0 atunci n-i-1 = ultimul element; cand i=1 atunci n-i-1 e penultimul element
    i += 1
print("inv = ", inv)  # printez pentru mine

if inv == sirCaractere:
    print("Sirul de caractere este Palindrom")
else:
    print("Sirul de caractere nu este Palindrom")
print("......................................................................................................")
print("De la Ciprian")
s = 'abc3443cba'

i, n = 0, len(s) - 1

while i < n:
    if s[i] != s[n]:
        print('Stringul nu este palindrom')
        break
    i += 1
    n -= 1
else:
    print('Stringul este palindrom')
print("......................................................................................................")