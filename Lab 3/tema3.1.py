from math import factorial

print("Exercitiul 3.1")

print("")
n = int(input("Tasteaza un numar: "))
if n < 0:
    print("Nu exista factorial de numar negativ.")
else:
    result = factorial(n)
    print("n! = ", result)
# print("...................................................")
n = int(input("Tasteaza un numar: "))
f = 1
for i in range(1, n+1):
    f = f * i
print("n! = ", f)
print("...................................................")
n = int(input("Write a number: "))
i=n-1
e=n
while i>0:
    n=n*(e-1)
    i=i-1
    e=e-1
print("n! =  ", n)
print("...................................................")
n = int(input("Write a number: "))
fact = 1
if n<0:
    print("Numarul trebuie sa fie pozitiv.")
elif n==0:
    print(1)
else:
   # fact = 1 o mai putem initializa si aici
    for i in range(1,n+1):
        fact=fact * i
    print("n! = ", fact)