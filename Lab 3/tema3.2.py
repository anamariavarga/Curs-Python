print("Exercitiul 3.2")

l = ['ABCD'[::-1], '12'[::-1], 'w'[::-1], ':-)'[::-1]][::-1]
print("Lista in oglinda este: ", l)
print("...................................................")
l = ['ABCD', '12', 'w', ':-)']
f=[]
for e in l[::-1]:
    f.append(e[::-1])
print("Lista in oglinda este: ", f)
print("...................................................")
l = ['ABCD', '12', 'w', ':-)']
f=[]
x=len(l)
y=1
while x>=1:
    f.insert(len(l)-x, l[len(l)-y][::-1])
    x=x-1
    y=y+1
print(f)
print("...................................................")
l = ['ABCD', '12', 'w', ':-)']
lst2=[]
for i in range(0,len(l)):
    ele = l[i][::-1]
    lst2.append(ele)
lst2.reverse()
print(lst2)
print("...................................................")
n= int(input("Enter number of elements: "))
lst=[]
lst2=[]
for i in range(0,n):
    ele = input(("Enter the element of the list: "))[::-1]
    lst.append(ele)
lst.reverse()
print(lst)