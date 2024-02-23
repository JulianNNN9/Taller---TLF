# Operaciones entre dos conjuntos
def union(conjunto1, conjunto2):
    # Unión de conjuntos
    resultado = [] # Inicializamos el restultado vacío
    for elemento in conjunto1: # Agregamos todos los elemetos del conjunto 1 al resultado
        resultado.append(elemento)
    for elemento in conjunto2: # Agregamos todos los elemetos del conjunto 2 al resultado
        if elemento not in resultado: # Se valida que no se repita un elemento previamente agregado por el conjunto 1
            resultado.append(elemento)
    return resultado # Retorna el resultado

def interseccion(conjunto1, conjunto2):
    # Intersección de conjuntos
    resultado = [] # Inicializamos el restultado vacío
    for elemento in conjunto1: # Recorre cada elemento del conjunto 1
        if elemento in conjunto2: # Si el elemento se encuentra en el conjunto 2 lo agrega al resultado
            resultado.append(elemento)
    return resultado # Retorna e resultado