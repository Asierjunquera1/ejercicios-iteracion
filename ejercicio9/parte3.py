def agregar_palabra(nueva_palabra, diccionario, siguiente, anterior):
    diccionario.append(nueva_palabra, -1, -1)
    indice_nueva_palabra = len(diccionario) - 1
    indice_actual = 0
    while diccionario[indice_actual].palabra < nueva_palabra and siguiente[indice_actual] != -1:
        indice_actual = siguiente[indice_actual]
    if diccionario[indice_actual].palabra > nueva_palabra:
        indice_anterior = anterior[indice_actual]
        siguiente[indice_anterior] = indice_nueva_palabra
        anterior[indice_actual] = indice_nueva_palabra
        siguiente[indice_nueva_palabra] = indice_actual
        anterior[indice_nueva_palabra] = indice_anterior
    else:
        anterior[indice_nueva_palabra] = indice_actual
        siguiente[indice_actual] = indice_nueva_palabra
    return diccionario
