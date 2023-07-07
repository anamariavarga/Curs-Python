print('Exercitiul 2.1 - Sa se afiseze toate literele mari din my_list')
print('')
print("Varianta 1")

my_list = list('ABcdEfghI')
for x in my_list:
    if x.isupper():
        print(x)

print(".............................................................................................")
print("Varianta 2")

#my_list = list('ABcdEfghI')
i = 0

while i <= len(my_list)-1:
    if my_list[i] >= 'A' and 'Z' >= my_list[i]:
        print(my_list[i])
    i += 1

print(".............................................................................................")
print("Varianta 3")
#my_list = list('ABcdEfghI')
i = 0

while i <= len(my_list)-1:
    if 'A' <= my_list[i] <= 'Z':
        print(my_list[i])
    i += 1
print(".............................................................................................")
print("De la Ciprian")
my_list = list('ABcdEfgZhI')

i = 0
while i < len(my_list):
    if 'A' <= my_list[i] <= 'Z':
        print(my_list[i])
    i += 1
print(".............................................................................................")
print("test git")
