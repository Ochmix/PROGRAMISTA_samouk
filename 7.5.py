lista1 = [1, 2, 3, 4]
lista2 = [4, 3, 2, 1]
lista3 = []
for i in lista1:
    for j in lista2:
        x = i*j
        lista3.append(x)

print(lista3)
