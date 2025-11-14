import random

def inserta_ordenado(lista_nombres: list[str], nombre: str) -> None:
    """
    Inserta un nombre en una lista de nombres manteniendo el orden (de menor a mayor longitud).
    Si la lista recibida no estuviera ordenada por longitud, la función no hace nada.

    Parámetros:
    lista_nombres (list[str]): Lista de nombres ordenada por longitud.
    nombre (str): Nombre a insertar.
    """
    lista_longitud=list()

    for n in lista_nombres.copy():
        lista_longitud.append(len(n))
    
    if lista_longitud==sorted(lista_longitud):
        if lista_longitud==[] or len(nombre)>=lista_longitud.pop():
            lista_nombres.append(nombre)
        else:
            for i,c in enumerate(lista_longitud):
             if len(nombre)<c:
                lista_nombres.insert(i,nombre)
                break
    
    else:
        return None


def busca_duplicados(lista: list) -> list:
    """
    Busca y devuelve una lista con los elementos duplicados en la lista recibida.

    Parámetros:
    lista (list): Lista en la que buscar duplicados.

    Devuelve:
    list: Lista con los elementos duplicados.
    """
    res=[]
    #for i in lista:
    #    if lista.count(i)>1 and (i in res)==False:
    #        res.append(i)
    i=0
    while i<=len(lista)-1:

        if lista[i] in lista[i+1:] and lista[i] not in res:
            res.append(lista[i])

        i+=1
    return res
    

def genera_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    """
    Genera una lista con n números enteros aleatorios en un rango dado,
    asegurando que no haya dos elementos consecutivos iguales.

    Parámetros:
    n (int): Número de elementos en la lista.
    minimo (int): Valor mínimo del rango (inclusive).
    maximo (int): Valor máximo del rango (inclusive).

    Devuelve:
    list[int]: Lista con n números enteros aleatorios.
    """

    res=[]

    while n!=0:
        n1= random.randint(minimo,maximo)
        n2= random.randint(minimo,maximo)
        if n1!=n2 and n1 not in res[-1:]:
            res.append(n1)
            res.append(n2)
            n-=2

    return res
        

    
    

def intercala_listas(lista1: list, lista2: list) -> list:
    """
    Intercala dos listas. Si una lista es mayor que la otra, los elementos sobrantes se añaden al final.

    Parámetros:
    lista1 (list): Primera lista.
    lista2 (list): Segunda lista.

    Devuelve:
    list: Lista resultante de intercalar las dos listas.
    """
    res=[]
    long1=len(lista1)
    long2=len(lista2)
    for i,j in zip(lista1,lista2):
        res.append(i)
        res.append(j)
    
    if long1>long2:
        if long2!=0:
            k=long1-long2
            while k<long1:
                res.append(lista1[k])
                k+=1
        else:
            res=lista1

    if long2>long1:
        if long1!=0:
            k=long2-long1
            while k<long2:
                res.append(lista2[k])
                k+=1
        else:
            res=lista2

    return res


def mezcla_ordenadas(lista1: list, lista2: list) -> list:
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    lista1 (list): Primera lista ordenada.
    lista2 (list): Segunda lista ordenada.

    Devuelve:
    list: Lista resultante de mezclar las dos listas ordenadas.
    """
    res=intercala_listas(lista1,lista2)
    return sorted(res)

def ordena_bubble_sort(lista: list) -> None:
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento bubble sort. 

    Parámetros:
    lista (list[int]): Lista de números enteros a ordenar.
    """    
    while True:
        ordenada=True
        for i,j in zip(lista,lista[1:]):
            if i>j:
                lista[lista.index(i)],lista[lista.index(j)+1]=j,i
                ordenada=False
        if ordenada == True:
            break

        
