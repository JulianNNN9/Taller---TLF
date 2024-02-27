# pyright: reportMissingImports=false
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3, venn3_circles


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

def diferencia(conjunto1, conjunto2):
    # Diferencia de conjuntos (conjunto1 - conjunto2
    resultado = [] # Inicializamos el restultado vacío
    for elemento in conjunto1: # Recorre cada elemento del conjunto 1
        if elemento not in conjunto2: # Si el elemento no se encuentra en el conjunto 2 se agrega al resultado
            resultado.append(elemento)
    return resultado # Retorna el resultado

def complemento(universo, conjunto):
    # Complemento de un conjunto en relación con un universo dado
    resultado = [] # Inicializamos el restultado vacío
    for elemento in universo: # Se recorre cada elemento del conjunto universal
        if elemento not in conjunto: # Si el elemento no se encuentra en el conjunto se agrega al resultado
            resultado.append(elemento)
    return resultado # Retorna el resultado

def combinacion(conjunto1, conjunto2):
    # Combinación de conjuntos
    resultado = [] # Inicializamos el restultado vacío
    for elemento1 in conjunto1: # Recorre cada elemento del conjunto 1
        for elemento2 in conjunto2: # Por cada elemento del conjunto 1, se le combina con cada elemento del conjunto 2
            resultado.append((elemento1, elemento2))
    return resultado # Retorna el resultado

# Cardinalidad
def calcular_cardinalidad(conjunto):

    cardinalidad = 0 # Inicializar un contador
    for _ in conjunto: # Iterar sobre los elementos del conjunto y aumentar el contador
        cardinalidad += 1
    
    return cardinalidad # Retornar la cardinalidad

# Subconjunto
def es_subconjunto(conjunto1, conjunto2):
    # Verificar si conjunto1 es subconjunto de conjunto2
    for elemento in conjunto1: # Recorre cada elemento del conjunto 1
        if elemento not in conjunto2: # Si se encuentra un elemento del conjunto 1 que no se encuentra en el conjunto 2, retorna False
            return False
    return True # Y si encuentra todos los elementos en el conjunto 2, retorna True

# Conjuntos disjuntos
def son_disjuntos(conjunto1, conjunto2):
    # Verificar si conjunto1 y conjunto2 son conjuntos disjuntos
    for elemento in conjunto1: # Recorre cada elemento del conjunto 1
        if elemento in conjunto2: # Si encuentra un elemento del conjunto 1 en el conjunto 2, retorna False
            return False
    return True # Y si no encuentra ningún elemento del conjunto 1 en el conjunto 2 retorna True

# Conjuntos
conjunto_A = set([1,2,3])
conjunto_B = set([3,4,5])
conjunto_C = set([5,6,7])

# Ejemplo 1: Intersección entre A y B
interseccion_AB = interseccion(conjunto_A, conjunto_B)

# Ejemplo 2: Diferencia entre A y C
diferencia_A_C = diferencia(conjunto_A, conjunto_C)

# Ejemplo 3: Unión de A y C
union_A_C = union(conjunto_A, conjunto_C)

# Crea el diagrama de Venn
venn_diagram = venn3([conjunto_A, conjunto_B, conjunto_C],
                    set_labels=('A', 'B', 'C'))

# Muestra el diagrama
plt.show()