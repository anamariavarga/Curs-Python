print('''Exercitiul 2.5 - Sa se verifice daca un sir de caractere citit de la tastatura este palindrom sau nu
Nu se tine cont de case-ul carcaterelor''')
print('')
sirCaractere = input('Tasteaza sirul de carctere care va fi evaluat: ')
if sirCaractere.upper() == sirCaractere[::-1].upper():
    print("Sirul de caractere este Palindrom")
else:
    print("Sirul de caractere nu este Palindrom")
print("......................................................................................................")
sirCaractere = input('Tasteaza sirul de carctere care va fi evaluat: ').upper()
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
sirCaractere = input('Tasteaza sirul de carctere care va fi evaluat: ')
if sirCaractere.lower() == sirCaractere[::-1].lower():
    print("Sirul de caractere este Palindrom")
else:
    print("Sirul de caractere nu este Palindrom")
print("......................................................................................................")
sirCaractere = input('Tasteaza sirul de carctere care va fi evaluat: ').lower()
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
s = 'aBc3443cba'

# case insensitive
s = s.lower()

if s == s[::-1]:
    print('Stringul este palindrom')
else:
    print('Stringul nu este palindrom')
print("......................................................................................................")
