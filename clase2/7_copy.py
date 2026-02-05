lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]
lista1.append(456789)
lista1.append("Hola Mundo")
lista2.append("Hola y adiós")
lista2.append(5555)
lista3 = lista1[:-1]
lista4 = lista2[1:-1]
lista5 = lista3.copy()
lista5.append(lista4)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")
print(lista3)
print(f"Lista 4: {lista4}")
print(f"Lista 5: {lista5}")