###################################################################################################
# Universidad del Valle de Guatemala
# Paola de León
# Paola Contreras 
###################################################################################################

import itertools as conteo;

# Todos diferentes
print("\n____________________________________________________________________________________________________")
print("\n       -> Ejercicio 1.A\n")
print("Genere las sucesiones de 4 dígitos diferentes e imprima su conteo")
A = list(conteo.permutations('0123456789', 4))
print("R/. " + str(len(A)))


print("\n____________________________________________________________________________________________________")
print("\n       -> Ejercicio 1.B\n")
print("Genere las secesiones de 4 dígitos que contengan uno o más dígitos repetidos e imprima su conteo")
setA = set(A)
setAll = set(conteo.product('0123456789', repeat = 4))
# Tomar diferencia del conjunto setAll
B = setAll.difference(setA)
print("R/. " + str(len(list(B))))



print("\n____________________________________________________________________________________________________")
print("\n       -> Ejercicio 1.C.1\n")
print("Repetición de 4 dígitos")
repeatAll = []
# Recorrer lista obteniendo objetos
for i in B:
    repeat = 0
    # Recorrer tuplas según posición
    for j in range(3):
        before = i[j]
        after = i[j+1]
        # Comparar valores de valor actual con posterior
        if before == after:
            repeat = repeat + 1
    
    # Verificar que todos los números se repitan
    if repeat == 3:
        repeatAll.append(i)

print("R/. " + str(len(repeatAll)))

print("\n____________________________________________________________________________________________________")
print("\n       -> Ejercicio 1.C.2\n")
print("Repetición de 2 dígitos 2 veces cada uno")
repeatTwoAll = []
for i in B:
    tempos = []
    # Recorrer tuplas según posición
    for j in range(4):
        # Contar cantidad de repeticiones de valor
        if (i.count(i[j])==2):
            # Agregar valor a lista temporal
            if i[j] not in tempos:
                tempos.append(i[j])
                
    # Verificar cantidad de números repetidos
    if (len(tempos) == 2):
        repeatTwoAll.append(i)

print("R/. " + str(len(repeatTwoAll)))
    

print("\n____________________________________________________________________________________________________")
print("\n       -> Ejercicio 1.C.3\n")
print("Repetición de 3 dígitos")
repeatTwo = []
for i in B:
    tempos = []
    # Recorrer tuplas según posición
    for j in range(4):
        # Contar cantidad de repeticiones de valor
        if (i.count(i[j])==2):
            # Agregar valor a lista tempral
            if i[j] not in tempos:
                tempos.append(i[j])
                
    # Verificar cantidad de números repetidos
    if len(tempos) == 1:
        repeatTwo.append(i)

print("R/. " + str(len((repeatTwo))))




print("\n____________________________________________________________________________________________________")
print("\n       -> Ejercicio 1.C.4\n")
repeatThree = []
for i in B:
    tempos = []
    # Recorrer tuplas según posición
    for j in range(3):
        # Contar cantidad de repeticiones de valor
        if (i.count(i[j])==3):
            # Agregar valor a lista tempral
            if i[j] not in tempos:
                tempos.append(i[j])
                
    # Verificar cantidad de números repetidos
    if len(tempos)==1:
        repeatThree.append(i)

print("R/. " + str(len(repeatThree)))