# 2. Folosind funcția map și o funcție lambda scrieți o expresie care sa transforme lista asta
# [2, 8, 5, -3, 0] în asta [4, 64, 25, 9, 0]
l1 = [2, 8, 5, -3, 0]
l2 = list(map(lambda x: x**2,l1))
print(l2)
print("****************************************************")
#daca am ca input o lista de stringuri
l = ['2', '8',' 5', '-3', '0']
l3 = list(map(lambda y: int(y)**2 , l))
print(l3)
print("****************************************************")
# daca vreau ca rezutatul sa fie o lista de stringuri
l = ['2', '8',' 5', '-3', '0']
l3 = list(map(lambda y: str(int(y)**2) , l))
print(l3)
print("****************************************************")
# daca vreau sa sortez lista de stringuri dar ca pe int-uri
l = ['2', '8',' 5', '-3', '0']
l3 = list(map(lambda y: str(int(y)**2) , l))
print(sorted(l3, key=int))
