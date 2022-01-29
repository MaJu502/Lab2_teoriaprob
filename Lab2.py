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


def Ejercicio2():
    print("Se despliega ejercicio 2:")


def Ejercicio3():
    print("Se despliega ejercicio 3:")

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

                        # Forme un conjunto con las tuplas en el orden requerido
                        tupla = (i5, i4, i3, i2, i1)
                        listaTupla.append(tupla)

    # Conteo de elementos de la tupla
    elementosTupla = len(listaTupla)

    # Valor de K
    print("Valor de K: ", k)

    # Verificacion de K
    print("Verificacion de K (conteo de lista con tuplas): ", elementosTupla)

    combReemplazo = str(
        len([i for i in conteo.combinations_with_replacement('1234567', 5)]))

    # Verificacion con combinación con reemplazo
    print("Combinación con reemplazo: ",
          combReemplazo)

    if k == combReemplazo:
        print("La diferencia de elementos es 0")

    else:
        print("La diferencia de elementos no es 0.")

    """
    COMENTARIO:
    
    """


# --------------- Main -------------------


def bye():
    print('Gracias por usar el programa!!')


print('\n----- Bienvenido al programa ----\n')

menu = 0

dict_menu = {
    '1': Ejercicio1,
    '2': Ejercicio2,
    '3': Ejercicio3,
    '4': bye
}

while menu != '4':

    menu = input(
        '\ningrese una opcion\n1. Ejercicio 1\n2. Ejercicio 2\n3. Ejericio 3\n4. salir\n-> ')
    accion = dict_menu[menu]
    accion()
