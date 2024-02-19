"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]
    suma = [int(fila[1]) for fila in archivo]
    return sum(suma)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from collections import Counter

    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    letras = [fila[0] for fila in archivo]
    cantidad = dict(Counter(letras))
    final = sorted(cantidad.items())

    return final


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    letrasNumeros = [(fila[0], int(fila[1])) for fila in archivo]
    letrasSuma = {fila[0]:0 for fila in archivo}
    for i in letrasNumeros:
        if i[0] in letrasSuma.keys():
            letrasSuma[i[0]] += i[1]
   
    final = sorted(letrasSuma.items())
    return final


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    fechas = [fila[2].split('-')[1] for fila in archivo]
    fechas = dict(Counter(fechas))
    final = sorted(fechas.items())

    return final

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    letras = sorted({fila[0] for fila in archivo})
    letraNumero = [(fila[0], int(fila[1])) for fila in archivo]

    minmax = {letra: [] for letra in letras}
    for i in letraNumero:
        minmax[i[0]].append(i[1])
    
    x = []
    for i in minmax:
        x.append((i, max(minmax[i]), min(minmax[i])))

    return x


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t")[4].split(",") for z in archivo]
    letras = sorted({palabra[:3] for diccionario in archivo for palabra in diccionario})
    letras = {letra: [] for letra in letras}

    for i in archivo:
        for elemento in i:
            letras[elemento[:3]].append(int(elemento[4:]))

    x = []
    for i in letras:
        x.append((i, min(letras[i]), max(letras[i])))

    return x

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    columnas = [(fila[0], int(fila[1])) for fila in archivo]
    numeros = sorted([fila[1] for fila in columnas])
    numeros = {numero: [] for numero in numeros}

    for i in columnas:
        numeros[i[1]].append(i[0])

    x = []
    for j in numeros:
        x.append((j, numeros[j]))

    return x



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    columnas = [(fila[0], int(fila[1])) for fila in archivo]
    numeros = sorted([fila[1] for fila in columnas])
    numeros = {numero: [] for numero in numeros}

    for i in columnas:
        if i[0] not in numeros[i[1]]:
            numeros[i[1]].append(i[0])

    x = []
    for j in numeros:
        x.append((j, sorted(numeros[j])))

    return x

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from collections import Counter

    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t")[4].split(",") for z in archivo]
    letras = sorted(palabra[:3] for diccionario in archivo for palabra in diccionario)
    letras = dict(Counter(letras))
    return letras


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """

    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]
    columnas = [[col[0], col[3].split(","), col[4].split(",") ] for col in archivo]

    x = []
    for elemento in columnas:
        x.append((elemento[0], len(elemento[1]), len(elemento[2])))

    return x


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]
    letras = sorted({letra for col in archivo for letra in col[3].split(",")})
    
    final = {letra:0 for letra in letras}

    for i in archivo:
        l = i[3].split(",")
        for elemento in l:
            final[elemento] += int(i[1])
    
    return final


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    archivo = open('data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    letras = sorted({fila[0] for fila in archivo})
    col5 = [[col[0],col[4].split(",")] for col in archivo]

    for fila in col5:
        for elemento in range(len(fila[1])):
            fila[1][elemento] = int(fila[1][elemento][4:])
        fila[1] = sum(fila[1])
    
    dicc = {letra: 0 for letra in letras}

    for elemento in col5:
        dicc[elemento[0]] += elemento[1]

    return dicc

