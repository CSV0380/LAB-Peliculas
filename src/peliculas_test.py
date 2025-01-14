from peliculas import *

def test_lee_peliculas(ruta):
    print("Test de lee_peliculas:")
    print(f"Total registros leídos: {len(lee_peliculas(ruta))}")
    print(f"Mostrando los tres primeros registros: {lee_peliculas(ruta)[:2]}")





if __name__ == '__main__':
    test_lee_peliculas("data\peliculas.csv")