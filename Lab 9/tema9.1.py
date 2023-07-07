# 1. Avem o lista de genul acesta (conține tuple cu cate doua elemente numere)
l = [(5, 21), (6, 11), (0, 25), (-6, 6)]
# Sortati lista după criteriul produsului dintre cele doua elemente numere ale tuplelor. Sortarea listei ar trebui sa arate asa:
# [(-6, 6), (0, 25), (6, 11), (5, 21)] pentru ca produsele celor doua elemente ale fiecărei tuple ar arăta așa:
# -36 0 66 105 deci sunt sortate crescator
# Folosiți sorted și parametrul key la care îi pasati o funcție lambda. Încercați și cu funcție clasică dacă nu va iese cu lambda.

print(sorted(l, key=lambda a: a[0] * a[1]))
