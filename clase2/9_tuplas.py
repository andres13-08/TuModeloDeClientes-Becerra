tuplas_anidadas = ((1, 2), (10, 20))

#Me dice cuántos elementos tiene esta tupla 1. (1,2) y 2. (10,20)
print(len(tuplas_anidadas))

#Muestrame el primero elemento de esta tupla, que al ser 0, es decir el primer elemento. 
print(tuplas_anidadas[0])

#Para acceder al primer elemento de la primera tupla.
uno = tuplas_anidadas[0][0]
print(uno)

#Para que me mjestre el último elemento de una tupla. Ammbas validas. 
print(tuplas_anidadas[1][1])
print(tuplas_anidadas[-1][-1])