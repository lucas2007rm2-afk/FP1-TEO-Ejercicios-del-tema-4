import csv
from collections import namedtuple
import datetime

Pelicula = namedtuple('Pelicula', [
    "fecha_estreno",   # tipo date
    "titulo",          # tipo str
    "director",        # tipo str
    "genero",          # tipo list[str]
    "duracion",        # tipo int
    "presupuesto",     # tipo int
    "recaudacion",     # tipo int
    "reparto"          # tipo list[str]
])

def lee_peliculas(ruta_fichero: str) -> list[Pelicula]:    
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # Saltamos la cabecera
        peliculas=[]
        for fecha_estreno,titulo,director,genero,duracion,presupuesto,recaudacion,reparto in lector:

            fecha_estreno=datetime.date.fromisoformat(fecha_estreno)
            genero=list(genero.split(","))
            duracion=int(duracion)
            presupuesto=int(presupuesto)
            recaudacion=int(recaudacion)
            reparto=list(reparto.split(","))

            pelicula=Pelicula(fecha_estreno,titulo,director,genero,duracion,presupuesto,recaudacion,reparto)
            peliculas.append(pelicula)
    
    return peliculas

def existe_pelicula(peliculas: list[Pelicula], cadena_en_titulo: str) -> bool:
    """
    Comprueba si existe alguna película cuyo título contenga la cadena dada.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    cadena_en_titulo (str): Cadena a buscar en los títulos de las películas.
    Devuelve:
    bool: True si existe al menos una película cuyo título contiene la cadena, False en caso
    contrario.
    """
    for pelicula in peliculas:
        if cadena_en_titulo in pelicula.titulo:
            return True
        
    return False
    

def son_todas_director_genero(peliculas: list[Pelicula], director: str, genero: str) -> bool:
    """
    Comprueba si todas las películas del director dado pertenecen al género indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    director (str): Nombre del director.
    genero (str): Género a comprobar.
    Devuelve:
    bool: True si todas las películas del director pertenecen al género, False en caso contrario.
    """
    for pelicula in peliculas:
        if pelicula.director == director:
            if genero not in pelicula.genero:
                return False
            
    return True

def construye_lista_titulos_actor(peliculas: list[Pelicula], actor: str) -> list[str]:
    """
    Devuelve una lista de títulos en los que el actor indicado aparece en el reparto.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    actor (str): Nombre del actor.
    Devuelve:
    list[str]: Lista de títulos de películas en las que aparece el actor.
    """    
    lista_titulos=[]

    for pelicula in peliculas:
        if actor in pelicula.reparto:
            lista_titulos.append(pelicula.titulo)

    return lista_titulos
    

def calcula_presupuesto_total_año(peliculas: list[Pelicula], año: int) -> int:
    """
    Suma y devuelve el presupuesto total de las películas cuyo año de estreno es el indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    año (int): Año de estreno.
    Devuelve:
    int: Presupuesto total de las películas estrenadas en el año indicado.
    """
    presupuesto_total=0

    for p in peliculas:
        if año == p.fecha_estreno.year:
            presupuesto_total+=p.presupuesto

    return presupuesto_total

def encuentra_pelicula_mayor_recaudacion(peliculas: list[Pelicula], genero: str) -> Pelicula | None:
    """
    Devuelve la película con mayor recaudacion entre las que incluyen el genero dado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    genero (str): Género a buscar.
    Devuelve:
    Pelicula | None: Película con mayor recaudación del género indicado, o None si no existe ninguna.
    """

    mayor_recaudacion=0
    pelicula_mayor_recaudacion=None

    for p in peliculas:
        if genero in p.genero:
            if mayor_recaudacion==0 or p.recaudacion>mayor_recaudacion:
                mayor_recaudacion=p.recaudacion
                pelicula_mayor_recaudacion=p

    return pelicula_mayor_recaudacion

    





