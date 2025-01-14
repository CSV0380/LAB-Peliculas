from datetime import date, datetime
from typing import NamedTuple, List, Tuple, Dict
import csv
from collections import defaultdict

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos", list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)


#APARTADO 1 (1 punto)

def lee_peliculas(ruta:str) -> List[Pelicula]:
    peliculas = list()
    with open(ruta, mode = 'r', encoding = 'utf-8')as fichero:
        lector = csv.reader(fichero, delimiter = ';')
        next(lector)
        for e in lector:
            fecha_estreno = datetime.strptime(e[0], "%d/%m/%Y").date()
            titulo = str(e[1])
            director = str(e[2])
            generos = [genero.strip() for genero in e[3].split(',')] #  cuidado con esto que da errores si no lo pones 
            duracion = int(e[4])
            presupuesto = int(e[5])
            recaudacion = int(e[6])
            reparto = [reparto.strip() for reparto in e[7].split(',')]
            peliculas.append(Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto))
        return peliculas


#APARTADO 2 (1 punto)

def peliculas_mas_ganancias(lista: List[Pelicula], genero: str = None) -> Tuple[str, int]:
    res = []
    for pelicula in lista:
        if genero in pelicula.generos or genero is None:
            res.append((pelicula.titulo, pelicula.recaudacion - pelicula.presupuesto))

    ordenadas = sorted(res, key = lambda x: x[1], reverse = 'True')[:1]
    return ordenadas    
    

#APARTADO 3 (1.5 puntos)

def media_presupuesto_por_genero(peliculas: List[Pelicula]) -> Dict[str, float]:
    genero_presupuesto = defaultdict(list)  # Diccionario con listas para acumular presupuestos por género
    
    for pelicula in peliculas:
        for genero in pelicula.generos:
            genero_presupuesto[genero].append(pelicula.presupuesto) # a la clave genero le das el valor presupuesto
    
    # Calcular la media de presupuesto para cada género
    return {genero: sum(presupuestos) / len(presupuestos) for genero, presupuestos in genero_presupuesto.items() if presupuestos} # lo pone entre corchetes para hacer un dict
           #pones la clave : lo que quieres


#APARTADO 4 (1.5 puntos)

def peliculas_por_actor(lista: List[Pelicula], año_inicial: int = None, año_final: int = None) -> Dict[str, int]:
    peliculas = defaultdict(int)  # Diccionario para contar las participaciones
    
    for pelicula in lista:
        # Asegúrate de obtener el año como entero
        año_estreno = pelicula.fecha_estreno.year  # Asegúrate de que fecha_estreno es un objeto datetime.date
        if (año_inicial is None or año_estreno >= año_inicial) and (año_final is None or año_estreno <= año_final):
            for actor in pelicula.reparto:
                peliculas[actor] += 1  # Incrementar el contador para cada actor
    
    return sorted(dict(peliculas).items(), key = lambda x: x[1], reverse = True)



def actores_mas_frecuentes(lista: List[Pelicula], n: int, año_inicial: int = None, año_final: int = None) -> 


if __name__ == '__main__':
    #print(f"{lee_peliculas("data\\peliculas.csv")}")

    datos = lee_peliculas("data\\peliculas.csv")

    #print(f"{peliculas_mas_ganancias(datos, "Drama")}")

    #print(f"{media_presupuesto_por_genero(datos)}")

    print(f"{peliculas_por_actor(datos, 2005, 2019)}")
