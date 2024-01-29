import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

"""
Puedes pensar que las llaves del defaultdict representan las
posiciones en el vector disperso, mientras que los valores representan
los elementos en esas posiciones.  Cualquier clave que esté ausente en
el dict significa que ese elemento en el vector disperso está ausente
(es cero).

Ten en cuenta que el tipo de llave utilizada no debería afectar al
algoritmo.  Puedes imaginar que las llaves son índices enteros (como
0, 1, 2) en el vector disperso, pero también debe funcionar igual con
llaves arbitrarias (como "red", "blue", "green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


def find_alphabetically_first_word(text: str) -> str:
    """
    Dada una cadena |text|, devuelve la palabra en |text| que aparece
    primero lexicográficamente (es decir, la palabra que aparecería
    primero después de ordenarlas). Una palabra se define por una
    secuencia máxima de caracteres sin espacios en blanco. Puede que
    min() te resulte útil aquí. Si el texto de entrada es una cadena
    vacía, es aceptable devolver una cadena vacía o generar un error.
    """
    # INICIO
    
    palabras = text.split()  
    primera_palabra = min(palabras, key=str)
    
    return primera_palabra
    # FIN


def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Regresa la distancia Euclidiana entre dos ubicaciones,
    representadas como una pareja de enteros (por ejemplo (3, 5)).
    """
    # INICIO
    
    x1, y1 = loc1
    x2, y2 = loc2

    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

    return distance

    # FIN


def mutate_sentences(sentence: str) -> List[str]:
    """
    Dada una oración (secuencia de palabras), regresa una lista de
    todas las palabras "similares".
    Definimos que una oración es "similar" a la original si
      - tiene la misma cantidad de palabras, y
      - cada pareja de palabras adyacentes en la nueva oración también
        aparece en la oración original (las palabras de cada par deben
        aparecer en el mismo orden en la oración de salida que en la
        oración original).
    Notas:
      - El orden de las oraciones que produces no importa.
      - No debes producir duplicados.
      - La oración generada puede usar una palabra de la oración
        original más de una vez.
    Por ejemplo:
      - Entrada: 'the cat and the mouse'
      - Salida: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
    """
    # INICIO
    raise Exception("Not implemented yet")
    # FIN


def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Dados dos vectores dispersos |v1| y |v2|, cada uno representado
    como collections.defaultdict(float), regresa su producto punto.

    Puedes encontrar útil usar sum() y una comprensión de lista.  Esta
    función será útil luego para clasificadores lineales.

    Nota: Los vectores dispersos son vectores donde la mayoría de sus
    elementos son 0.
    """
    # INICIO
   
    
    # FIN


def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector) -> None:
    """
    Dados dos vectores dispersos |v1| y |v2|, realiza el cálculo
    v1 += scale * v2.
    Si el valor de scale es cero, se admite modificar v1 para incluir
    cualquier llave adicional en v2, o simplemente no añadir llaves.

    Nota: Esta función debe MODIFICAR v1, pero no regresarlo.  No
    modifiques v2 en tu implementación.
    Esta función nos será útil mas adelante para clasificadores
    lineales.
    """
    # INICIO
    if scale != 0:
        for key in v2:
            v1[key] = v1.get(key, 0) + scale * v2[key]
    else:
        for key in v2:
            v1.setdefault(key, 0)
    # FIN


def find_nonsingleton_words(text: str) -> Set[str]:
    """
    Divide la cadena |text| por espacios en blanco y regresa el
    conjunto de palabras que aparecen más de una vez.
    Puedes encontrar útil usar collections.defaultdict(int).
    """
    # INICIO
    raise Exception("Not implemented yet")
    # FIN
