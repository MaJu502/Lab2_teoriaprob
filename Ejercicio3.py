###################################################################################################
# Universidad del Valle de Guatemala
# Alejandro Gómez
# Cristian Aguirre
###################################################################################################

# Import de la librería de itertools
import itertools as conteo

# Variables brindadas en problema
n = 7
m = 5
k = 0

Tupla = ()
listaTupla = []

# For brindado en el problema
for i1 in range(1, n+1):  # 1-7
    for i2 in range(1, i1+1):  # i- i1
        for i3 in range(1, i2+1):  # i -i2
            for i4 in range(1, i3+1):  # i-i3
                for i5 in range(1, i4+1):  # i-i4

                    #k = k + 1
                    k += 1
                    tupla = (i5, i4, i3, i2, i1)
                    listaTupla.append(tupla)

elementosTupla = len(listaTupla)
# Valor de K
print("Valor de K: ", k)
print("Verificacion de K (conteo de lista con tuplas): ", elementosTupla)
