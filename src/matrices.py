def suma_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Suma dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la suma.
    """
    for i,j in zip(m1,m2):
        if len(i)!=len(m1[0]) or len(j)!=len(m2[0]):
            return None
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        return None
    
    res=[]

    for i,j in zip(m1,m2):
        res.append([])
        for x,y in zip(i,j):
            res[m1.index(i)].append(x+y)

    return res

def multiplica_matrices(m1: list[list[int | float]], m2: list[list[int | float]]) -> list[list[int | float]]:
    """
    Multiplica dos matrices y devuelve el resultado.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]]: Matriz resultante de la multiplicación.
    """
    for i,j in zip(m1,m2):
        if len(i)!=len(m1[0]) or len(j)!=len(m2[0]):
            return None
    if len(m1[0])!=len(m2):
        return None
    
    res=crear_matriz(len(m1),len(m2[0]))

    for i,x in enumerate(m1):
        for j,y in enumerate(x):
            for k,z in enumerate(m2[j]):
                res[i][k]+=y*z
                
    return res



def crear_matriz(filas:int,columnas:int)->list[list[int]]:
    """
    Crea una matriz de ceros para la multiplicación de matrices
    """

    res=[]

    for i in range(0,filas):
        res.append([])
        for j in range(0,columnas):
            res[i].append(0)
    
    return res

    

