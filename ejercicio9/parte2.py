class Palabra:
    def __init__(self, palabra, anterior, siguiente):
        self.palabra = palabra
        self.anterior = anterior
        self.siguiente = siguiente

def listar_palabras(letra, diccionario):
    lista = []
    i = 0
    while i < len(diccionario) and diccionario[i].palabra[0] < letra:
        i = diccionario[i].siguiente
    while i < len(diccionario) and diccionario[i].palabra[0] == letra:
        lista.append(diccionario[i].palabra)
        i = diccionario[i].siguiente
    return lista
