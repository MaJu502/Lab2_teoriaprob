
# lista donde se guardaran los numeros primos
primos:list = []

for i in range(1, 101):

    # Se incluyen los numeros de 1 al 100
    primos.append(i)
    
    # Se excluye el numero 1
    if i == 1:
        primos.remove(i) 

    # Se excluyen los numeros multiplos de 2 mayores que 2
    elif i % 2 == 0 and i != 2:
        primos.remove(i) #quita el elemento de la lista primos

    # Se excluyen los numeros multiplos de 3 mayores que 3
    elif i % 3 == 0 and i != 3:
        primos.remove(i)
    
    # Se excluyen aquellos numeros multiplos de 5
    elif i % 5 == 0 and i != 5:
        primos.remove(i)

    # Se excluyen aquellos numeros multiplos de 7
    elif i % 7 == 0 and i != 7:
        primos.remove(i)   


print(f'Lista de numeros primos < 100: \n{primos}\nlargo: {len(primos)}') # Imprime lista de numeros primos menores a 100