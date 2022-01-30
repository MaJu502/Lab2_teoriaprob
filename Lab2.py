"""
Universidad del Valle de Guatemala
Teoría de Probabilidades sección 
13/01/2022

Miembros:
Alejandro Gómez - 20347
Diego Córdova - 20212
Cristian Aguirre - 20231
Paola de León - 20361
Paola Contreras - 20213
Marco Jurado - 20308

"""

# Import de la librería de itertools
import itertools as conteo

# --------------- Ejercicio 1 -------------------
""" Se define la primera función para el Ejercicio 1"""


def Ejercicio1():
    print("Se despliega ejercicio 1:")
    # Todos diferentes
    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\n       -> Ejercicio 1.A\n")
    print("Genere las sucesiones de 4 dígitos diferentes e imprima su conteo")
    A = list(conteo.permutations('0123456789', 4))
    print("R/. " + str(len(A)))

    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\n       -> Ejercicio 1.B\n")
    print(
        "Genere las secesiones de 4 dígitos que contengan uno o más dígitos repetidos e imprima su conteo"
    )
    setA = set(A)
    setAll = set(conteo.product('0123456789', repeat=4))
    # Tomar diferencia del conjunto setAll
    B = setAll.difference(setA)
    print("R/. " + str(len(list(B))))

    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\n       -> Ejercicio 1.C.1\n")
    print("Repetición de 4 dígitos")
    repeatAll = []
    # Recorrer lista obteniendo objetos
    for i in B:
        repeat = 0
        # Recorrer tuplas según posición
        for j in range(3):
            before = i[j]
            after = i[j + 1]
            # Comparar valores de valor actual con posterior
            if before == after:
                repeat = repeat + 1

        # Verificar que todos los números se repitan
        if repeat == 3:
            repeatAll.append(i)

    print("R/. " + str(len(repeatAll)))

    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\n       -> Ejercicio 1.C.2\n")
    print("Repetición de 2 dígitos 2 veces cada uno")
    repeatTwoAll = []
    for i in B:
        tempos = []
        # Recorrer tuplas según posición
        for j in range(4):
            # Contar cantidad de repeticiones de valor
            if (i.count(i[j]) == 2):
                # Agregar valor a lista temporal
                if i[j] not in tempos:
                    tempos.append(i[j])

        # Verificar cantidad de números repetidos
        if (len(tempos) == 2):
            repeatTwoAll.append(i)

    print("R/. " + str(len(repeatTwoAll)))

    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\n       -> Ejercicio 1.C.3\n")
    print("Repetición de 3 dígitos")
    repeatTwo = []
    for i in B:
        tempos = []
        # Recorrer tuplas según posición
        for j in range(4):
            # Contar cantidad de repeticiones de valor
            if (i.count(i[j]) == 2):
                # Agregar valor a lista tempral
                if i[j] not in tempos:
                    tempos.append(i[j])

        # Verificar cantidad de números repetidos
        if len(tempos) == 1:
            repeatTwo.append(i)

    print("R/. " + str(len((repeatTwo))))

    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\n       -> Ejercicio 1.C.4\n")
    repeatThree = []
    for i in B:
        tempos = []
        # Recorrer tuplas según posición
        for j in range(3):
            # Contar cantidad de repeticiones de valor
            if (i.count(i[j]) == 3):
                # Agregar valor a lista tempral
                if i[j] not in tempos:
                    tempos.append(i[j])

        # Verificar cantidad de números repetidos
        if len(tempos) == 1:
            repeatThree.append(i)

    print("R/. " + str(len(repeatThree)))


def Ejercicio2():
    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\nSe despliega ejercicio 2:")

    primos: list = []  # lista donde se guardaran los numeros primos
    count = conteo.count(1, 1)  # count de 1 en 1

    # Se recorren los numeros del 1 al 100 en el count
    for i in count:

        # Se excluye el numero 1
        if i == 1:
            continue

        # Se excluyen los numeros multiplos de 2 mayores que 2
        elif i % 2 == 0 and i != 2:
            continue

        # Se excluyen los numeros multiplos de 3 mayores que 3
        elif i % 3 == 0 and i != 3:
            continue

        # Se excluyen aquellos numeros multiplos de 5
        elif i % 5 == 0 and i != 5:
            continue

        # Se excluyen aquellos numeros multiplos de 7
        elif i % 7 == 0 and i != 7:
            continue

        # Se evitan los numeros mayores que 100
        if i >= 100:
            break

        # Se incluyen unicamente los numeros primos de 1 al 100
        primos.append(i)

    print(
        f'Lista de numeros primos < 100: \n{primos}\nConteo de numeros primos menores a 100: {len(primos)}'
    )  # Imprime lista de numeros primos menores a 100


def Ejercicio3():
    print(
        "\n____________________________________________________________________________________________________"
    )
    print("\nSe despliega ejercicio 3:")

    # Variables brindadas en problema
    n = 7
    m = 5
    k = 0

    Tupla = ()
    listaTupla = []

    # For brindado en el problema
    for i1 in range(1, n + 1):  # 1-7
        for i2 in range(1, i1 + 1):  # i- i1
            for i3 in range(1, i2 + 1):  # i -i2
                for i4 in range(1, i3 + 1):  # i-i3
                    for i5 in range(1, i4 + 1):  # i-i4

                        #k = k + 1
                        k += 1

                        # Forme un conjunto con las tuplas en el orden requerido
                        tupla = (i5, i4, i3, i2, i1)
                        listaTupla.append(tupla)

    # Conteo de elementos de la tupla
    elementosTupla = len(listaTupla)

    # Valor de K
    print("Valor de K: ", k)

    # Cantidad de elementos en lista tupla
    print("Cantidad de elementos de la lista: ", elementosTupla)

    # Conjunto de muestras de 5 elementos de 7 elementos con reemplazo
    combReemplazo = str(
        len([i for i in conteo.combinations_with_replacement('1234567', 5)]))

    # Despliegue de combinación con reemplazo
    print("Combinación con reemplazo: ", combReemplazo)

    # Se castea k como string para comparar
    k = str(k)

    # Se verifica lo obtenido
    if k == combReemplazo:
        print("El valor de k es:", k,
              "al igual que el valor de la combinacion de reemplazo: ",
              combReemplazo)
        print("Por lo tanto, la diferencia existente entre ambas es de 0.")

    else:
        print("La diferencia de elementos no es 0.")


# --------------- Main -------------------


def bye():
    print('Gracias por usar el programa!!')


print('\n----- Bienvenido al programa ----\n')

menu = 0

dict_menu = {'1': Ejercicio1, '2': Ejercicio2, '3': Ejercicio3, '4': bye}

while menu != '4':

    try:
        menu = input(
            '\ningrese una opcion\n1. Ejercicio 1\n2. Ejercicio 2\n3. Ejericio 3\n4. Salir\n-> '
        )
        accion = dict_menu[menu]
        accion()

    except KeyError:
        print('ERROR: Eliga una opcion valida')
