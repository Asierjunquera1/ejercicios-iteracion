def raiz_cuadrada_entera(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    r = n // 2
    while r > n // r:
        r = (r + n // r) // 2

    return r


    raiz_cuadrada_entera(25)
