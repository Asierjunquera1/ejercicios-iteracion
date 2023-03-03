def cuadrados_perfectos(lim):
    lista=[]
    i=0
    while i**2<lim:
        lista.append(i**2)
        i+=1
    return lista


