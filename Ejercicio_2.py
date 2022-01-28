

# Se importa la libreria itertools
import itertools

primos:list = [] # lista donde se guardaran los numeros primos
conteo = itertools.count(1, 1) # Conteo de 1 en 1
    
# Se recorren los numeros del 1 al 100 en el conteo
for i in conteo:
    
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


print(f'Lista de numeros primos < 100: \n{primos}\nConteo de numeros primos menores a 100: {len(primos)}') # Imprime lista de numeros primos menores a 100
