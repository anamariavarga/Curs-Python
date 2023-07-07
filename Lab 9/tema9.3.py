# 3. Folosind funcția map și o funcție lambda scrieți o expresie care sa transforme
# listele acestea: [2, 3, 1] [1, 4, 5] ['A', 'q', '#'] în asta ['AAA', 'qqqqqqq', '######']
l1 = [2, 3, 1]
l2 = [1, 4, 5]
l3 = ['A', 'q', '#']
l_final = list(map(lambda x, y, z: (x+y) * z,l1,l2,l3))
print(l_final)
print('***********************************************')
l1 = [2, 3, 1]
l2 = [1, 4, 5]
l3 = ['A', 'q', '#']
l_final = list(map(lambda x: (x[0] + x[1]) * x[2], zip(l1,l2,l3)))
ls =list( zip(l1,l2,l3))
print(ls)
print(l_final)