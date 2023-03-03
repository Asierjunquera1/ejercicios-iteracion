def listar_palabras(letra, diccionario, siguiente, anterior):
    lista = []
    i = 0
    while i < len(diccionario) and diccionario[i][0] < letra:
        i = siguiente[i]
    while i < len(diccionario) and diccionario[i][0] == letra:
        lista.append(diccionario[i])
        i = siguiente[i]
    return lista



